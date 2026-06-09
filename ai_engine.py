import ollama

def generate_content(topic):
    prompt = f"""
    You are a viral YouTube Shorts script writer.

    Generate:
    1. 3 catchy YouTube titles
    2. 1 short viral script (max 120 words)
    3. 1 SEO description
    4. 5 hashtags

    Topic: {topic}
    """

    response = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': prompt}]
    )

    return response['message']['content']