from flask import Flask
from textprocessing import get_response

app = Flask(__name__)


@app.route("/")
def output():
    return "Hello World!"


if __name__ == "__main__":
    app.run("0.0.0.0", "5010")
