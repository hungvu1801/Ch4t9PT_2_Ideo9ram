import copy
from config import URL_API, PAYLOAD, HEADERS, MESSAGES
from dotenv import load_dotenv
import json
import os
import requests

def message_generator(user_prompt, previous_content=None):
    messages = copy.deepcopy(MESSAGES)
    if not previous_content:
        # System content
        messages[0]["content"] = "You are a helpful assistant."
    else:
        messages.append({"role": "assistant", "content": previous_content})
    messages[1]["content"] = user_prompt
    return messages

def request_chatGPT_API(user_prompt, max_token=None, previous_content=None):
    load_dotenv()
    # define headers
    API_KEY = os.environ.get("OPENAI_API_KEY")
    headers = copy.deepcopy(HEADERS)
    payload = copy.deepcopy(PAYLOAD)
    
    headers["Authorization"] = f"Bearer {API_KEY}"
    # print(headers)
    # Define payload
    if max_token:
        payload["max_tokens"] = max_token
    messages = message_generator(user_prompt, previous_content)
    payload["messages"] = messages
    # print(payload)
    # Make API call
    response = requests.post(URL_API, headers=headers, data=json.dumps(payload))

    # Check if the request was successful
    result = ""
    if response.status_code == 200:
        # Parse the response and print the message
        parsed_response = response.json()
        result = parsed_response['choices'][0]['message']['content']
    else:
        # Print the error if something went wrong
        print(f"Error: {response.status_code}")
    return result


