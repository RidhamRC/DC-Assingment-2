import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

def get_db_connection():
    print("\n\n\n\n")
    print(DATABASE_URL)
    return psycopg2.connect(DATABASE_URL)