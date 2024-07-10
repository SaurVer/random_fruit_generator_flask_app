from flask import Flask, jsonify
import random

app = Flask(__name__)

FRUITS = [
    "Apple",
    "Banana",
    "Cherry",
    "Date",
    "Elderberry",
    "Fig",
    "Grape",
    "Honeydew",
    "Imbe",
    "Jackfruit",
    "Kiwi",
    "Lemon",
    "Mango",
    "Nectarine",
    "Orange",
    "Papaya",
    "Quince",
    "Raspberry",
    "Strawberry",
    "Tangerine",
]


@app.route("/")
def random_fruit():
    fruit = random.choice(FRUITS)
    return jsonify({"fruit": fruit})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
