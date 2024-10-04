from flask import Flask, jsonify

app = Flask(__name__)

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(app.static_folder, 'favicon.ico')

@app.route('/api/empty', methods=['GET'])
def empty():
    return jsonify({"message": "This color does not belong to me..."})

if __name__ == '__main__':
    app.run(debug=True)