import os
from groq import Groq

# Replace with your actual Groq API key if not using environment variables
api_key = os.getenv("GROQ_API_KEY", "YOUR_GROQ_API_KEY_HERE")

client = Groq(api_key=api_key)
models = client.models.list()

print("\n--- Available Groq Models ---")
for m in models.data:
    print(f"- {m.id}")