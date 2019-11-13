from flask import Flask, render_template, flash, request, redirect
import textprocessing

app = Flask(__name__)

# Handles requests made to server
@app.route("/", methods=["GET", "POST"])
def output():
    try:
        # Handles GET request (likely from browser) by redirecting to github
        if request.method == "GET":
            return redirect("https://github.com/manukastratta/DeText", code=303)

        # Handles POST request (from extension)
        if request.method == "POST":
            # request.values.get('html') — this accesses the HTML data sent by extension
            text = textprocessing.text_from_html(request.values.get('html'))
            print(text)
            # Return sends a JSON back to the extension – format {key: value, key_2: value, ... key_n: value}
            return {
                "text": text
            }

        # # For testing purposes, make request to server from browser to compare with request to server from extension
        # elif request.method == "GET":
        #     url = "https://github.com/manukastratta/DeText2"
        #     return textprocessing.get_response(url)

    # In case of server error
    except Exception as e:
        return flash(e)


# Starts server
if __name__ == "__main__":
    app.run()
