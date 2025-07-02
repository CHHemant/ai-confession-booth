from flask import Flask, render_template, request, session, jsonify
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"

responses = [
    "🤖 AI says: Everyone copies from Stack Overflow. You are forgiven.",
    "🔥 AI says: Pushing to main? Sacrilege! May your bugs be many.",
    "👀 AI says: Print statements are the true debugging tools. Proceed.",
    "🌍 AI says: It works on your machine? Then it works in production... right?",
    "🧪 AI says: No tests? You live dangerously! I respect that.",
    "😂 AI says: I hope your rubber duck understands you better than your code reviewers.",
    "📛 AI says: Confess again, sinner. The AI is amused."
]

roasts = [
    "👹 AI says: That’s a spicy confession! Repent by writing 10 more unit tests.",
    "💾 AI says: Did you just commit secrets? Go wash your hands.",
    "🦠 AI says: Your code has been quarantined."
]

memes = [
    "https://media.giphy.com/media/3o7qE1YN7aBOFPRw8E/giphy.gif",
    "https://media.giphy.com/media/l0MYEqEzwMWFCg8rm/giphy.gif",
    "https://media.giphy.com/media/3o7TKxoh7rXbD8VqTu/giphy.gif"
]

@app.route("/", methods=["GET"])
def index():
    history = session.get("history", [])
    return render_template("index.html", history=history)

@app.route("/confess", methods=["POST"])
def confess():
    confession = request.form["confession"]
    outcome = random.choice(["forgive", "roast", "meme"])
    if outcome == "forgive":
        reply = random.choice(responses)
        meme_url = ""
    elif outcome == "roast":
        reply = random.choice(roasts)
        meme_url = ""
    else:
        reply = "😂 AI sends you a meme:"
        meme_url = random.choice(memes)

    # Save to session history
    history = session.get("history", [])
    history.append({"confession": confession, "reply": reply, "meme": meme_url})
    if len(history) > 10:
        history = history[-10:]  # Keep only last 10 confessions
    session["history"] = history

    return jsonify({"reply": reply, "meme": meme_url})

if __name__ == "__main__":
    app.run(debug=True)
