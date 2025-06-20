from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        print("Incoming request data:", data)  # Debug print

        if not data or "message" not in data:
            return jsonify({"error": "Message field is required"}), 400

        message = data["message"]

        # Example reply (replace with actual OpenAI logic if needed)
        reply = f"Received your message: {message}"
        return jsonify({"reply": reply})

    except Exception as e:
        print("Error:", str(e))  # Debug print
        return jsonify({"error": "Invalid request format"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
