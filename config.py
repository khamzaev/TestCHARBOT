import os

TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN", "your-token-here")
POSTGRES_URL = os.getenv("POSTGRES_URL", "postgresql+asyncpg://your_db")

