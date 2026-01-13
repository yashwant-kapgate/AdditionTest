from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    num1 = data.get('num1')
    num2 = data.get('num2')

    if num1 is None or num2 is None:
        return jsonify({"error": "Please provide num1 and num2"}), 400

    result = num1 + num2

    return jsonify({
        "num1": num1,
        "num2": num2,
        "result": result
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
