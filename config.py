import os
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден в .env")

CPU_THRESHOLD = 85
RAM_THRESHOLD = 90
DISK_THRESHOLD = 90

CHECK_INTERVAL = 30