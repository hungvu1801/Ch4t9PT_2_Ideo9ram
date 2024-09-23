from src.chat_gpt import request_chatGPT_API

def main() -> None:
    prompt = "Please make the title for the above created prompt"
    print(request_chatGPT_API(prompt, 100))