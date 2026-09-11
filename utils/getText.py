import json
import requests

headers = {
    "Authorization": ""}

url = "https://api.edenai.run/v2/text/code_generation"


def getResult(instruction):
    payload = {
        "providers": "google",
        "prompt": "",
        "instruction": instruction,
        "temperature": 0.1,
        "max_tokens": 500,
        "fallback_providers": ""
    }
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    text = result['google']['generated_text']
    try:
        output = rawToText(text)
        return output
    except ValueError:
        return text


def rawToText(text: str):
    first = text.index("`")
    second = text.index("`", first + 3)
    return text[first + 9:second]
