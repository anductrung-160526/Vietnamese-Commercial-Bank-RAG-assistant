"""
evaluate.py
-----------
Chạy đánh giá hệ thống RAG bằng RAGAs.

Quy trình:
1. Với mỗi câu hỏi trong gold set: gọi RAG, lưu lại (câu trả lời, ngữ cảnh).
2. Đưa toàn bộ vào RAGAs để chấm 4 chỉ số:
   - faithfulness:        câu trả lời có bịa không
   - answer_relevancy:    câu trả lời có đúng trọng tâm không
   - context_precision:   ngữ cảnh có sạch không
   - context_recall:      ngữ cảnh có đủ không
3. Xuất kết quả ra CSV + in bảng tóm tắt ra terminal.

Chạy:
    python -m evaluation.evaluate
"""

import os
import sys
import time
from datetime import datetime

import pandas as pd
from datasets import Dataset

from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall,
)
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Cho phép import từ thư mục gốc của dự án
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config
from rag_chain import build_qa_chain, ask
from evaluation.gold_set import GOLD_SET


def collect_predictions(qa_chain):
    """Chạy RAG trên toàn bộ gold set, thu thập câu trả lời và ngữ cảnh."""
    print(f"Đang chạy RAG trên {len(GOLD_SET)} câu hỏi...")
    rows = []
    for i, item in enumerate(GOLD_SET, 1):
        question = item["question"]
        ground_truth = item["ground_truth"]

        try:
            answer, source_docs = ask(qa_chain, question)
            contexts = [doc.page_content for doc in source_docs]
        except Exception as e:
            print(f"  [{i}] LỖI: {e}")
            answer = ""
            contexts = []

        rows.append({
            "question": question,
            "answer": answer,
            "contexts": contexts,
            "ground_truth": ground_truth,
        })
        print(f"  [{i}/{len(GOLD_SET)}] {question[:60]}...")
        # Nhịp nhỏ để tránh rate-limit
        time.sleep(0.3)

    return rows


def run_ragas(rows):
    """Đưa kết quả vào RAGAs để chấm điểm."""
    print("\nĐang chấm điểm bằng RAGAs (có thể mất vài phút)...")

    dataset = Dataset.from_list(rows)

    # RAGAs cần LLM + embeddings để chấm. Bọc qua wrapper để hỗ trợ
    # proxy openai_api_base (ví dụ shopaikey, OpenRouter, Azure...).
    judge_llm = LangchainLLMWrapper(
    ChatOpenAI(
        model=config.LLM_MODEL,
        temperature=0.1,
        openai_api_key=config.OPENAI_API_KEY, # Thêm dòng này nếu cần
        openai_api_base=config.OPENAI_API_BASE,
    )
)
    judge_embeddings = LangchainEmbeddingsWrapper(
        OpenAIEmbeddings(
            model=config.EMBEDDING_MODEL,
            openai_api_base=getattr(config, "OPENAI_API_BASE", None),
        )
    )

    result = evaluate(
        dataset=dataset,
        metrics=[
            faithfulness,
            answer_relevancy,
            context_precision,
            context_recall,
        ],
        llm=judge_llm,
        embeddings=judge_embeddings,
    )
    return result


def save_and_summarize(result, rows):
    """Lưu kết quả ra CSV và in tóm tắt."""
    df = result.to_pandas()

    # Tên file có timestamp để giữ lịch sử các lần chạy
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("evaluation/results", exist_ok=True)
    out_path = f"evaluation/results/ragas_{ts}.csv"
    df.to_csv(out_path, index=False)

    # In bảng tóm tắt
    print("\n" + "=" * 60)
    print("KẾT QUẢ ĐÁNH GIÁ RAGAs")
    print("=" * 60)

    metric_cols = [
        "faithfulness",
        "answer_relevancy",
        "context_precision",
        "context_recall",
    ]
    present = [c for c in metric_cols if c in df.columns]
    summary = df[present].mean().round(3)
    print(summary.to_string())

    print(f"\nChi tiết đã lưu: {out_path}")

    # Liệt kê những câu có điểm thấp để dễ debug
    print("\n--- 3 câu có faithfulness THẤP nhất (cần xem lại) ---")
    if "faithfulness" in df.columns:
        worst = df.nsmallest(3, "faithfulness")[
            ["question", "faithfulness", "answer_relevancy"]
        ]
        for _, row in worst.iterrows():
            print(f"  • [{row['faithfulness']:.2f}] {row['question'][:80]}")

    return df


def main():
    config.check_api_key()
    print("=== Bắt đầu đánh giá hệ thống RAG ===\n")

    qa_chain = build_qa_chain()
    rows = collect_predictions(qa_chain)
    result = run_ragas(rows)
    save_and_summarize(result, rows)

    print("\n=== Hoàn tất! ===")


if __name__ == "__main__":
    main()
