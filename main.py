from flask import Flask, request, jsonify

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

    return jsonify({
        "num1": num1,
        "num2": num2,
        "result": num1 + num2
    })
    
@app.route('/sub', methods=['POST'])
def sub_numbers():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    num1 = data.get('num1')
    num2 = data.get('num2')

    if num1 is None or num2 is None:
        return jsonify({"error": "Please provide num1 and num2"}), 400
    
    if num1 < num2:
        return jsonify({"error": "num1 should be greater than num2"}), 400

    return jsonify({
        "num1": num1,
        "num2": num2,
        "result": num1 - num2
    })
@app.route('/')
def health():
    return "Service is running", 200
if __name__ == '__main__':
    app.run(debug=True)