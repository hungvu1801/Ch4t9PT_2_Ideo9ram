from openai import OpenAI

def main() -> None:
    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        # {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Please Say this is a test."}
    ]
    )

    print(completion.choices[0].message)
    print(completion._request_id)