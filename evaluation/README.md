# 📊 Đánh giá hệ thống RAG với RAGAs

Module này giúp **đo lường định lượng** chất lượng hệ thống RAG thay vì
chỉ "hỏi thử rồi cảm nhận". Đây là bước rất quan trọng — không đo được
thì không biết cải tiến có thực sự hiệu quả hay không.

## 🎯 Bốn chỉ số đo

| Chỉ số | Đo gì | Đo phần nào |
|---|---|---|
| **Faithfulness** | Câu trả lời có bịa thông tin không | Generation |
| **Answer Relevancy** | Câu trả lời có đúng trọng tâm câu hỏi không | Generation |
| **Context Precision** | Top-k chunk truy hồi có sạch (không nhiễu) không | Retrieval |
| **Context Recall** | Truy hồi có lấy đủ thông tin cần không | Retrieval |

Mỗi điểm trong khoảng [0, 1]. **>= 0.8 thường được coi là tốt.**

Nếu Faithfulness thấp → LLM đang bịa → siết prompt hoặc đổi model.
Nếu Context Recall thấp → đang bỏ sót chunk → tăng `TOP_K`, chỉnh `chunk_size`,
hoặc thêm Hybrid Search.

## 📁 Cấu trúc

```
evaluation/
├── gold_set.py             # Bộ câu hỏi-đáp án chuẩn (20 câu mẫu)
├── evaluate.py             # Script chạy đánh giá
├── visualize.py            # Vẽ biểu đồ
├── requirements-eval.txt   # Thư viện riêng cho phần evaluation
├── results/                # Tự sinh: file CSV chi tiết theo lần chạy
└── charts/                 # Tự sinh: biểu đồ PNG
```

## 🚀 Cách dùng

### 1. Cài thêm thư viện đánh giá

```bash
pip install -r evaluation/requirements-eval.txt
```

### 2. Đảm bảo đã build vector index

Nếu chưa chạy `python ingest.py` thì chạy trước.

### 3. Chạy đánh giá

```bash
python -m evaluation.evaluate
```

Script sẽ:
1. Lần lượt hỏi 20 câu trong `gold_set.py` qua hệ thống RAG.
2. Gọi RAGAs (dùng LLM) để chấm 4 chỉ số.
3. In bảng tóm tắt ra terminal và lưu CSV chi tiết vào `evaluation/results/`.

Thời gian: ~3-5 phút cho 20 câu (tuỳ tốc độ API).

### 4. Vẽ biểu đồ

```bash
python -m evaluation.visualize
```

Tạo 2 file ảnh trong `evaluation/charts/`:
- `latest.png` — bar chart 4 chỉ số của lần chạy gần nhất.
- `history.png` — line chart so sánh các lần chạy (xuất hiện khi có ≥ 2 lần).

## 🔄 Quy trình cải tiến đề xuất

```
Đo (RAGAs)  →  Thấy điểm thấp ở đâu?
       ↓
Đề xuất cải tiến (chỉnh chunk_size, đổi model, thêm rerank...)
       ↓
Áp dụng + ingest lại
       ↓
Đo lại  →  So sánh với lần trước  →  Giữ hay bỏ?
```

Đây chính là vòng lặp **data-driven** mà nhà tuyển dụng muốn thấy ở
một Data Scientist Intern.

## 💡 Gợi ý mở rộng gold set

Bộ 20 câu hiện tại chỉ là mẫu. Để đánh giá thuyết phục hơn, bạn nên có
**30-50 câu** bao quát:

- Câu **dễ** (đáp án xuất hiện nguyên văn trong 1 chunk).
- Câu **trung bình** (cần tổng hợp 2-3 chunk).
- Câu **khó** (suy luận, so sánh giữa các sản phẩm).
- Câu **bẫy** (đáp án không có trong tài liệu — kiểm tra khả năng "từ chối").

Tỷ lệ khuyến nghị: 50% dễ, 30% trung bình, 10% khó, 10% bẫy.

## 📝 Cách trình bày trong CV / phỏng vấn

> Xây dựng pipeline đánh giá tự động cho hệ thống RAG bằng framework
> RAGAs với 4 chỉ số (faithfulness, answer relevancy, context precision,
> context recall) trên bộ 20 câu hỏi tự xây. Đạt **{điểm trung bình}**
> sau khi tinh chỉnh `chunk_size` và `top_k` qua 3 vòng cải tiến.

Số liệu cụ thể luôn ăn điểm hơn mô tả định tính.
