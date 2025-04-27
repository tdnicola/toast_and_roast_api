from flask import Flask, jsonify
from insults import generate_insult
from compliments import generate_compliment

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Toast and Roast API!"

@app.route('/insult', methods=['GET'])
def insult():
    return jsonify({
        "type": "insult",
        "message": generate_insult()
    })

@app.route('/compliment', methods=['GET'])
def compliment():
    return jsonify({
        "type": "compliment",
        "message": generate_compliment()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
