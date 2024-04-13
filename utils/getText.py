import json
import requests

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiN2M0ODBhNDQtYjVmMS00MzMwLWE0YzQtN2E0ZTMwNWFiZDg3IiwidHlwZSI6ImFwaV90b2tlbiJ9.tbsK1tlK5IatXO9e_b8Y0_Ze9QFV9sX52iV9BzZ7Ybo"}

url = "https://api.edenai.run/v2/text/code_generation"


def getResult(instruction):
    payload = {
        "providers": "openai",
        "prompt": "",
        "instruction": instruction,
        "temperature": 0.1,
        "max_tokens": 500,
        "fallback_providers": ""
    }
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    text = result['openai']['generated_text']
    try:
        output = rawToText(text)
        return output
    except ValueError:
        return text


def rawToText(text: str):
    first = text.index("`")
    second = text.index("`", first + 3)
    return text[first + 9:second]
