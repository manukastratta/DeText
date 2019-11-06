from flask import Flask
import textprocessing


app = Flask(__name__)


@app.route("/")
def output():

    return textprocessing.get_response("https://learn.adafruit.com/micropython-basics-loading-modules/import-code")


if __name__ == "__main__":
    app.run()
