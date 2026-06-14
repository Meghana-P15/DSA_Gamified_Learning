from flask import Flask, render_template, request, jsonify
import random 

app = Flask(__name__)

# Game memory cache setup
number = 0
attempts = 0
max_attempts = 0

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/mind")
def mind():
    return render_template("mindgame.html")

@app.route("/start", methods=["POST"])
def start():
    global number, attempts, max_attempts

    data = request.get_json() or {}
    level = data.get("level", "medium")
    attempts = 0

    if level == "easy":
        number = random.randint(1, 50)
        max_attempts = 15
        range_text = "1 to 50"
    elif level == "medium":
        number = random.randint(1, 100)
        max_attempts = 10
        range_text = "1 to 100"
    else:
        number = random.randint(1, 100)
        max_attempts = 5
        range_text = "1 to 100"

    return jsonify({
        "msg": "Game Started!",
        "range": range_text,
        "left": max_attempts
    })

@app.route("/guess", methods=["POST"])
def guess():
    global attempts, number, max_attempts

    data = request.get_json() or {}
    if "guess" not in data or data["guess"] == "":
        return jsonify({"msg": "Invalid Input!", "left": max_attempts - attempts, "end": False})
        
    user = int(data["guess"])
    attempts += 1
    diff = abs(user - number)
    left = max_attempts - attempts

    if user == number:
        return jsonify({"msg": "🎉 You won!", "end": True})

    if attempts >= max_attempts:
        return jsonify({"msg": f"💀 Lost! The number was {number}", "end": True})

    if left <= 3:
        if diff <= 2:
            msg = "🔥 Very close!"
        elif diff <= 5:
            msg = "Close!"
        else:
            msg = "Hurry up!"
    else:
        if diff <= 2:
            msg = "Almost there!"
        elif diff <= 5:
            msg = "So close!"
        elif user < number:
            msg = "Go Higher!"
        else:
            msg = "Go Lower!"

    return jsonify({"msg": msg, "left": left, "end": False})

if __name__ == "__main__":
    app.run(debug=True)
