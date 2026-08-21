import os
from dotenv import load_dotenv
from google import genai

#Load environment variables
load_dotenv()

#Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

#Create Gemini client
client = genai.Client(api_key=api_key)

#generating reusable SQL functions for database operations
def generate_sql(question, database_context):
    """
    Generate SQL query based on the user's question
    and the database schema/context.
    """

    prompt = f"""
    You are an expert SQL generator.
    Your task is to convert the user's natural language question
    into a valid PostgreSQL SQL query.

    Database schema:
        {database_context}

    user question:
        {question}

    Rules:
    1. Generate only the SQL query.
    2. Do not explain the query.
    3. Do not use markdown code fences.
    4. Use only tables and columns that exist in the provided schema.
    5. Generate PostgreSQL-compatible SQL.
    """

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
    )

    return response.text.strip()
    

if __name__ == "__main__":
    from database.context import build_database_context
    
    database_context = build_database_context()
    
    question = "Show me all customers"
    
    sql = generate_sql(question, database_context)
    
    print("\nGenerated SQL:")
    print(sql)
    
    