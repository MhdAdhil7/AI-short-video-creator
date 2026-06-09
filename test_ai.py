import ollama

response = ollama.chat(
    model='llama3',
    messages=[
        {
            'role': 'user',
            'content': 'Give me 3 YouTube title ideas about a skeleton growing four arms'
        }
    ]
)

print(response['message']['content'])