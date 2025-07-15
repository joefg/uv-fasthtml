import os

from dotenv import load_dotenv

load_dotenv()

# Application settings

DEBUG = os.getenv("DEBUG", "True").lower() == "true"
