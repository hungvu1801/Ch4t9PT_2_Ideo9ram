from src.chat_gpt import request_chatGPT_API

def main() -> None:
    prompt = "Please create a prompt for design a print-on-demand product that includes both an illustration and a motivational quote use on ideogram"
    print(request_chatGPT_API(prompt, 100))