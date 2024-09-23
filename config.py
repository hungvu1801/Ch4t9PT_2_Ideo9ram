URL_API = "https://api.openai.com/v1/chat/completions"


PAYLOAD = {
    "model": "gpt-3.5-turbo",  # You can also use "gpt-4" if your key has access
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": ""}
    ],
    "max_tokens": 50
}


HEADERS = {
    "Content-Type": "application/json",
    "Authorization": ""
    }