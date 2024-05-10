import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT_TOKEN = os.getenv("TOKEN")
    BASE_URL = "https://www.google.com/finance/quote/USD-UAH"
