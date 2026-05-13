from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/getSettings", methods=["POST"])
def get_settings():

    data = request.json

    id_instance = data["idInstance"]
    api_token = data["apiTokenInstance"]

    url = f"https://api.green-api.com/waInstance{id_instance}/getSettings/{api_token}"

    response = requests.get(url)

    return jsonify(response.json())


@app.route("/getStateInstance", methods=["POST"])
def get_state():

    data = request.json

    id_instance = data["idInstance"]
    api_token = data["apiTokenInstance"]

    url = f"https://api.green-api.com/waInstance{id_instance}/getStateInstance/{api_token}"

    response = requests.get(url)

    return jsonify(response.json())


@app.route("/sendMessage", methods=["POST"])
def send_message():

    data = request.json

    id_instance = data["idInstance"]
    api_token = data["apiTokenInstance"]

    chat_id = data["chatId"]
    message = data["message"]

    url = f"https://api.green-api.com/waInstance{id_instance}/sendMessage/{api_token}"

    payload = {
        "chatId": f"{chat_id}@c.us",
        "message": message
    }

    response = requests.post(url, json=payload)

    return jsonify(response.json())


@app.route("/sendFileByUrl", methods=["POST"])
def send_file():

    data = request.json

    id_instance = data["idInstance"]
    api_token = data["apiTokenInstance"]

    chat_id = data["chatId"]
    file_url = data["fileUrl"]

    url = f"https://api.green-api.com/waInstance{id_instance}/sendFileByUrl/{api_token}"

    payload = {
        "chatId": f"{chat_id}@c.us",
        "urlFile": file_url,
        "fileName": "image.jpg"
    }

    response = requests.post(url, json=payload)

    return jsonify(response.json())


if __name__ == "__main__":
    # app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)