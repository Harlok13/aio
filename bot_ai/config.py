import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BOT_TOKEN = os.getenv("BOT_TOKEN")

AI_TOKEN = os.getenv("AI_TOKEN")

UKASSA_TOKEN = os.getenv("UKASSA_TOKEN")

# postgresql
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
DATABASE = os.getenv("DATABASE")
IP = os.getenv("IP")
PG_PORT = os.getenv("PG_PORT")
