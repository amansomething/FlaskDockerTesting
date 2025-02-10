import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def test():
    return 'Test!'


if __name__ == '__main__':
    host = os.environ.get("HOST", "0.0.0.0")
    port = os.environ.get("PORT", "8000")

    app.run(debug=True, host=host, port=port)
