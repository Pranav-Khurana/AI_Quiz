import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


class Config:

    # LOGS DIRECTORY
    LOGS_DIR = BASE_DIR / "logs"

    # GEMINI KEY
    GEMINI_KEY = os.getenv("GEMINI_KEY")

    @staticmethod
    def check_logs_dir(LOGS_DIR):
        if not os.path.exists(LOGS_DIR):
            os.makedirs(LOGS_DIR)
