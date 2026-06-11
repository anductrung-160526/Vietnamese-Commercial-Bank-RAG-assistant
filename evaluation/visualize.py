"""
visualize.py
------------
Vẽ biểu đồ tóm tắt kết quả đánh giá để chèn vào README/báo cáo.

Hai biểu đồ:
1. Bar chart 4 chỉ số (lần chạy gần nhất).
2. Line chart so sánh nhiều lần chạy (theo dõi cải tiến qua thời gian).

Chạy:
    python -m evaluation.visualize
"""

import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

RESULTS_DIR = "evaluation/results"
OUT_DIR = "evaluation/charts"
METRICS = ["faithfulness", "answer_relevancy",
           "context_precision", "context_recall"]


def load_runs():
    """Đọc tất cả file CSV trong results/, mỗi file là một lần chạy."""
    files = sorted(glob.glob(f"{RESULTS_DIR}/ragas_*.csv"))
    if not files:
        raise FileNotFoundError(
            f"Chưa có kết quả trong {RESULTS_DIR}/. "
            "Hãy chạy `python -m evaluation.evaluate` trước."
        )
    runs = []
    for f in files:
        df = pd.read_csv(f)
        run_id = os.path.basename(f).replace("ragas_", "").replace(".csv", "")
        present = [m for m in METRICS if m in df.columns]
        means = df[present].mean()
        means["run"] = run_id
        runs.append(means)
    return pd.DataFrame(runs)


def plot_latest(latest_row):
    """Bar chart cho lần chạy mới nhất."""
    metrics = [m for m in METRICS if m in latest_row.index]
    values = [latest_row[m] for m in metrics]

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(metrics, values, color=["#2E86AB", "#A23B72", "#F18F01", "#C73E1D"])
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("Điểm (0-1)")
    ax.set_title(f"Kết quả RAGAs - lần chạy {latest_row['run']}")
    ax.axhline(y=0.8, color="gray", linestyle="--", alpha=0.5, label="Ngưỡng tốt (0.8)")
    ax.legend()

    # Hiển thị số trên đầu mỗi cột
    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 0.02,
                f"{v:.2f}", ha="center", fontweight="bold")

    plt.xticks(rotation=15)
    plt.tight_layout()
    out = f"{OUT_DIR}/latest.png"
    plt.savefig(out, dpi=120)
    print(f"Đã lưu: {out}")
    plt.close()


def plot_history(runs_df):
    """Line chart so sánh các lần chạy."""
    if len(runs_df) < 2:
        print("Chưa đủ lịch sử để vẽ biểu đồ so sánh (cần >= 2 lần chạy).")
        return

    fig, ax = plt.subplots(figsize=(10, 5))
    for m in METRICS:
        if m in runs_df.columns:
            ax.plot(runs_df["run"], runs_df[m], marker="o", label=m)
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("Điểm")
    ax.set_title("Diễn biến các chỉ số RAGAs qua các lần chạy")
    ax.legend(loc="lower right")
    ax.grid(alpha=0.3)
    plt.xticks(rotation=30)
    plt.tight_layout()
    out = f"{OUT_DIR}/history.png"
    plt.savefig(out, dpi=120)
    print(f"Đã lưu: {out}")
    plt.close()


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    runs = load_runs()
    print(f"Đã đọc {len(runs)} lần chạy.")
    plot_latest(runs.iloc[-1])
    plot_history(runs)


if __name__ == "__main__":
    main()
