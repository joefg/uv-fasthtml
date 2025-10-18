import os

from dotenv import load_dotenv

load_dotenv()

# Application settings
APP_NAME = os.getenv("APP_NAME", "uv-fasthtml")
FOOTER_TEXT = os.getenv("FOOTER_TEXT", "© uv-fasthtml, 2025 - all rights reserved")
PORT = os.getenv("PORT", 5001)

# Debug settings
DEBUG = os.getenv("DEBUG", 'false').lower() == "true"

# Datastore settings
DB_PATH = os.getenv("DB_PATH", "database/database.sqlite3")

# Telegram alert settings
TG_TOKEN = os.getenv("TG_TOKEN")
TG_ALERT_CHAT = os.getenv("TG_ALERT_CHAT")

# Discord alert settings
DISCORD_WEBHOOK_ID = os.getenv("DISCORD_WEBHOOK_ID")
DISCORD_WEBHOOK_TOKEN = os.getenv("DISCORD_WEBHOOK_TOKEN")

# Slack alert settings
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")