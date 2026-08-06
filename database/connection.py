import os
import psycopg2
from pathlib import Path
from dotenv import load_dotenv

#Load environment variables from .env file
env_path = Path(__file__).resolve().parent.parent / ".env"

print("Loading .env from:", env_path)

loaded = load_dotenv(dotenv_path=env_path, override=True)
print("Loaded:", loaded)

def get_connection():
    """
    Create and return a PostgreSQL database connection
    """
    
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )
        
        print("Connected to postgreSQL successfully!")
        return connection
    
    except Exception as e:
        print(f"Database Connection Error:{e}")
        return None
    
if __name__ == "__main__":
    conn = get_connection()
    
    if conn:
        conn.close()
        print("Database Connection closed.")
        