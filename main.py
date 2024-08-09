import os
import openai
from dotenv import load_dotenv

load_dotenv("keys.env")

openai.api_key = os.getenv("API_KEY")
print(openai.api_key)

# Definiere die Anfrage
def chat(input_text):
    response = openai.ChatCompletion.create(
        model="davinci-002",
        messages=[
            {"role": "user", "content": input_text},
        ]
    )
    return response.choices[0].message['content']

# Ausgabe der Antwort
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat(user_input)
        print("ChatGPT: ", response)
