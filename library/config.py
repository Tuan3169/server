import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get("KEY")
DATABASE_URI = os.environ.get("DATABASE_URL")
