import requests, uuid, json

key = "816d4add16a84b22b82697bd78515fc0"
endpoint = "https://api.cognitive.microsofttranslator.com/translate"
location = "japaneast"

constructed_url = endpoint

params = {
    "api-version": "3.0",
    "from": "en",
    "to": ["ja"]
}

headers = {
    "Ocp-Apim-Subscription-Key": key,
    "Ocp-Apim-Subscription-Region": location,
    "Content-type": "application/json",
    "X-ClientTraceId": str(uuid.uuid4),
}

body = [{'text': 'I would really like to drive your car around the block a few times.'}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
print(request)
response = request.json()
print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))