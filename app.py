from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

# Load environment variables (like your API key from .env)
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "✅ Diet Chatbot API is running!"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_prompt = data.get('prompt', '')

        if not user_prompt:
            return jsonify({'error': 'Prompt is required'}), 400

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or gpt-4 if your API key allows
            messages=[
                {"role": "system", "content": "You are a diet and nutrition expert chatbot. Answer user queries in a helpful, clear, and professional manner."},
                {"role": "user", "content": user_prompt}
            ]
        )

        message = response['choices'][0]['message']['content'].strip()
        return jsonify({'response': message})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 🔥 THIS is the part that tells Render to expose a port
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
