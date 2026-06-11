"""
config.py
---------
Tập trung mọi cấu hình của dự án vào một nơi để dễ chỉnh sửa.
API key được đọc từ biến môi trường (file .env) — KHÔNG hard-code key vào code.
"""

import os
from dotenv import load_dotenv

# Đọc các biến từ file .env (nếu có)
load_dotenv()

# ---- API KEY ----
# Đặt OPENAI_API_KEY trong file .env hoặc biến môi trường hệ thống.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = "https://api.shopaikey.com/v1" 

# ---- Đường dẫn ----
DATA_DIR = "data"            # Thư mục chứa tài liệu nguồn
INDEX_DIR = "faiss_index"    # Thư mục lưu vector index

# ---- Tham số chia nhỏ tài liệu (chunking) ----
# chunk_size lớn -> nhiều ngữ cảnh nhưng dễ lẫn nhiễu.
# chunk_size nhỏ -> sạch nhưng dễ mất ngữ cảnh.
# overlap giúp câu trả lời không bị cắt ngang giữa hai chunk.
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# ---- Tham số mô hình ----
EMBEDDING_MODEL = "text-embedding-3-small"  # Model tạo vector embedding
LLM_MODEL = "gpt-4o"                        # Model sinh câu trả lời
TEMPERATURE = 0                             # 0 = trả lời ổn định, ít "bịa"
TOP_K = 10                                  # Số chunk lấy ra cho mỗi câu hỏi


def check_api_key():
    """Kiểm tra API key trước khi chạy, báo lỗi thân thiện nếu thiếu."""
    if not OPENAI_API_KEY:
        raise EnvironmentError(
            "Chưa thiết lập OPENAI_API_KEY.\n"
            "Hãy tạo file .env (xem .env.example) hoặc chạy:\n"
            '  export OPENAI_API_KEY="sk-..."'
        )
