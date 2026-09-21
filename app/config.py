import os

from dotenv import load_dotenv

load_dotenv()

# Debug settings
DEBUG = os.getenv("DEBUG", 'false').lower() == "true"
TESTING = os.getenv("TESTING", 'false').lower() == "true"

# Application settings
APP_NAME = os.getenv("APP_NAME", "uv-fasthtml")
APP_DESCRIPTION = os.getenv("APP_DESCRIPTION", "A FastHTML template")
FOOTER_TEXT = os.getenv("FOOTER_TEXT", "© uv-fasthtml, 2026 - all rights reserved")
PORT = os.getenv("PORT", 5001)
DB_CONNECTION = os.getenv("DB_CONNECTION", "sqlite:///database/database.sqlite3")

# Telegram alert settings
TG_TOKEN = os.getenv("TG_TOKEN")
TG_ALERT_CHAT = os.getenv("TG_ALERT_CHAT")

# GitHub OAuth
GH_OAUTH_ID = os.getenv("GH_OAUTH_ID")
GH_OAUTH_SECRET = os.getenv("GH_OAUTH_SECRET")
