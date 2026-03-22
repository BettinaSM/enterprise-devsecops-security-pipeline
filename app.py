import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

APP_PASSWORD = os.getenv("APP_PASSWORD")

@app.route("/")
def home():
    return "Enterprise DevSecOps Security App Running"

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if not data or "password" not in data:
        return jsonify({"error": "Invalid request"}), 400

    if data["password"] == APP_PASSWORD:
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "denied"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
