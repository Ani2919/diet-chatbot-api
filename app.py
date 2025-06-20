from flask import Flask, request, jsonify
from flask_cors import CORS
import openai  # optional, currently not used

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(force=True)
        print("Incoming request data:", data)  # 🔍 Debugging line

        message = data.get("message")
        if not message:
            return jsonify({"error": "Message field is required"}), 400

        # 💬 Dummy reply for now
        reply = f"Received your message: {message}"
        return jsonify({"reply": reply})

    except Exception as e:
        print("Error occurred:", str(e))
        return jsonify({"error": "Invalid request", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
