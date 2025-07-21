# File: app.py
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    prompt = f"""
    You're a Gen Z gossip bot 🤭. Reply in a juicy, chaotic, emoji-filled, bestie-style tone.

    User: {user_message}
    Bot:
    """

    try:
        response = model.generate_content(prompt)
        reply = response.text
        return jsonify({"reply": reply})
    except Exception as e:
        import traceback
        traceback.print_exc()  # prints full error trace in terminal
        return jsonify({"reply": "Oops bestie, I dropped the tea cup ☕😩 Try again later!"})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

