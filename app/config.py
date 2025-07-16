import os

from dotenv import load_dotenv

load_dotenv()

# Application settings
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# Datastore settings
DB_PATH = os.getenv("DB_PATH", "database/database.db")
