from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    print("Received data:", data)  # <--- add this line for debugging

    message = data.get("message")
    if not message:
        return jsonify({"error": "Message field is required"}), 400

    reply = f"Received your message: {message}"
    return jsonify({"reply": reply})

