from flask import Flask, render_template, flash, request, redirect
import textprocessing


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def output():
    try:
        if request.method == "GET":
            return redirect("https://github.com/manukastratta/DeText", code=303)
        if request.method == "POST":
            text = textprocessing.text_from_html(request.values.get('html'))
            return {
                "text": text
            }
    except Exception as e:
        return flash(e)


if __name__ == "__main__":
    app.run()
