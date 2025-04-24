import openai
from dotenv import load_dotenv
import os
import time
from openai.error import RateLimitError

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except RateLimitError:
        print("Rate limit exceeded. Please wait and try again later.")
        time.sleep(10)  # Wait before retrying
        return "I'm currently unavailable. Please try again later."

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_with_gpt(user_input)
        print(f"GPT-3.5: {response}")