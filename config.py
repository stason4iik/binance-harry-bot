import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_ID = os.getenv("TELEGRAM_ID")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

BINANCE_PROFILE = os.getenv("BINANCE_PROFILE")