"""
rag_chain.py
------------
Bước "Generation" của RAG: tải FAISS index đã tạo, ghép với LLM
qua một prompt ràng buộc để mô hình CHỈ trả lời dựa trên tài liệu
(giảm hiện tượng bịa thông tin - hallucination).

Module này được dùng lại bởi app.py (giao diện) và có thể test riêng.
"""

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_classic.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

import config

# Prompt ép mô hình bám sát ngữ cảnh. Nếu không có thông tin -> nói rõ "không tìm thấy".
PROMPT_TEMPLATE = PromptTemplate(
    template=(
        "Bạn là một chuyên viên tư vấn khách hàng chuyên nghiệp của ngân hàng.\n"
        "Nhiệm vụ của bạn là giải đáp thắc mắc của khách hàng dựa trên phần 'Ngữ cảnh' được cung cấp.\n\n"
        "Yêu cầu:\n"
        "1. Trả lời đầy đủ, chi tiết và có cấu trúc rõ ràng (sử dụng gạch đầu dòng nếu cần).\n"
        "2. Chỉ sử dụng thông tin trong phần 'Ngữ cảnh'. Tuyệt đối không tự ý bịa đặt.\n"
        "3. Nếu không có thông tin trong ngữ cảnh, hãy lịch sự từ chối: 'Rất tiếc, tôi không tìm thấy thông tin cụ thể về vấn đề này trong tài liệu hướng dẫn.'\n\n"
        "Ngữ cảnh:\n{context}\n\n"
        "Câu hỏi của khách hàng: {question}\n\n"
        "Câu trả lời chi tiết (bằng tiếng Việt):" # <-- Đổi từ "ngắn gọn" thành "chi tiết"
    ),
    input_variables=["context", "question"],
)

def load_vectorstore():
    """Tải FAISS index đã lưu từ ingest.py."""
    embeddings = OpenAIEmbeddings(
        model=config.EMBEDDING_MODEL,
        openai_api_base=config.OPENAI_API_BASE,   # <-- THÊM DÒNG NÀY
    )
    return FAISS.load_local(
        config.INDEX_DIR,
        embeddings,
        allow_dangerous_deserialization=True,
    )


def build_qa_chain():
    """Tạo chuỗi hỏi-đáp RAG hoàn chỉnh."""
    config.check_api_key()
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": config.TOP_K})

    llm = ChatOpenAI(model=config.LLM_MODEL, temperature=config.TEMPERATURE,         openai_api_base=config.OPENAI_API_BASE # <--- THÊM DÒNG NÀY
)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,  # Trả về cả nguồn để hiển thị trích dẫn
        chain_type_kwargs={"prompt": PROMPT_TEMPLATE},
    )
    return qa_chain


def ask(qa_chain, question: str):
    """Hỏi một câu, trả về (câu trả lời, danh sách nguồn)."""
    result = qa_chain.invoke({"query": question})
    answer = result["result"]
    sources = result.get("source_documents", [])
    return answer, sources


# Cho phép test nhanh trong terminal: python rag_chain.py
if __name__ == "__main__":
    chain = build_qa_chain()
    print("Trợ lý đã sẵn sàng. Gõ 'exit' để thoát.\n")
    while True:
        q = input("Bạn hỏi: ").strip()
        if q.lower() in {"exit", "quit", ""}:
            break
        ans, srcs = ask(chain, q)
        print(f"\nTrả lời: {ans}")
        print("Nguồn: " + ", ".join(
            s.metadata.get("source", "?") for s in srcs
        ) + "\n")
