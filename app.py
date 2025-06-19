from flask import Flask, request, jsonify
import openai
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful diet and nutrition assistant who answers only in clear English using HTML tags like <p>, <h2>, etc."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    reply = response['choices'][0]['message']['content']
    return jsonify({"response": reply})
