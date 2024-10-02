from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/blue', methods=['GET'])
def blue():
    return jsonify({"message": "Hello, the color is blue!"})

@app.route('/api/empty', methods=['GET'])
def empty():
    return jsonify({"message": "This color does not belong to me..."})

if __name__ == '__main__':
    app.run(debug=True)
