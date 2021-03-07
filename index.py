import os

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    time_series = os.listdir("data_raw")
    images = os.listdir("static/images")
    return render_template(
        "index.html",
        time_series=time_series,
        images=reversed(images),
        title="Extended DFA transform",
    )


if __name__ == "__main__":
    app.run()
