from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder='../Web')

# Serve the index.html file
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Serve static files (CSS, JS, images, etc.)
@app.route('/<path:path>')
def serve_static_files(path):
    if os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

# API endpoint
@app.route('/api/message')
def get_message():
    return jsonify(message="Hello from the backend!")

if __name__ == '__main__':
    app.run(port=3000, debug=True)
