import os
from dotenv import load_dotenv
from google import genai

#Load environment variables
load_dotenv()

#Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

#Create Gemini client
client = genai.Client(api_key=api_key)

#Test Gemini
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Say hello in one sentence."
)

print(response.text)