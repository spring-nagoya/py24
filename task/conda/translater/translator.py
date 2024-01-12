import requests, uuid, json
from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
from dotenv import load_dotenv

load_dotenv()


key = os.environ["key"]
endpoint = "https://api.cognitive.microsofttranslator.com/translate"
location = "japaneast"


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/translate", methods=["POST"])
def translate():
    constructed_url = endpoint

    params = {
        "api-version": "3.0",
        "from": request.form.get["from_lang"],
        "to": [request.form.get("to_lang")],
    }

    headers = {
        "Ocp-Apim-Subscription-Key": key,
        "Ocp-Apim-Subscription-Region": location,
        "Content-type": "application/json",
        "X-ClientTraceId": str(uuid.uuid4),
    }

    body = [
        {"text": "I would really like to drive your car around the block a few times."}
    ]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    print(request)
    response = request.json()
    return render_template(
        "translate.html",
        res=json.dumps(
            response,
            sort_keys=True,
            ensure_ascii=False,
            indent=4,
            separators=(",", ": "),
        ),
    )
