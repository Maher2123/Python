import openai

# Setze deinen API-Schlüssel hier
openai.api_key = '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'

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
