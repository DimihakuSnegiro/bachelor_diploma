import os
from dotenv import load_dotenv

load_dotenv()

db_config = {
    "dbname": os.getenv("POSTGRES_DB"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "host": "localhost",
    "port": os.getenv("POSTGRES_PORT")
}