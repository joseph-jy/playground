from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/hello', methods=['GET'])
def api_hello():
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run()

