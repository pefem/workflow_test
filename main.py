from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>YES IT WORKS i told you</p>"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')