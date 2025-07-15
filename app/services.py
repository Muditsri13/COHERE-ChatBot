import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print("✅ API Key Loaded:", api_key[:8] + "..." if api_key else "❌ Not loaded")

client = OpenAI(api_key=api_key)

def ask_openai(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("❌ OpenAI API Error:", e)
        return f"Error contacting OpenAI: {e}"
