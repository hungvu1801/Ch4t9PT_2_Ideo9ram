import copy
from config import URL_API, PAYLOAD, HEADERS
from dotenv import load_dotenv
import json
import os
import requests

def request_chatGPT_API(message, max_token=None):
    load_dotenv()
    # define headers
    API_KEY = os.environ.get("OPENAI_API_KEY")
    headers = copy.deepcopy(HEADERS)
    headers["Authorization"] = f"Bearer {API_KEY}"
    # print(headers)
    # Define payload
    payload = copy.deepcopy(PAYLOAD)
    if max_token:
        payload["max_tokens"] = max_token
    payload["messages"][1]["content"] = message
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


