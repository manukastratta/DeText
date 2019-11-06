from flask import Flask, render_template, flash, request
import textprocessing


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def output():
    try:
        if request.method == "GET":
            return textprocessing.get_response("http://www.google.com")
        if request.method == "POST":
            # return "<h4>hello</h4>"
            return {
                "text": textprocessing.text_from_html(request.values.get('html'))
            }
    except Exception as e:
        return flash(e)


if __name__ == "__main__":
    app.run()
