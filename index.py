import os

from flask import Flask, render_template, request

from calc.aggregator import load_series
from calc.resulting import build_cd_dfa_graphics, build_dfa_graphics

app = Flask(__name__)


@app.route("/")
def index():
    time_series = os.listdir("data_raw")
    return render_template(
        "index.html", time_series=time_series, title="Extended DFA transform"
    )


@app.route("/graphics")
def result():
    path = request.args.get("jsdata")
    build_dfa_graphics(path)
    images = os.listdir("static/images")
    return render_template("graphics.html", images=reversed(images))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


def save_ts():  # pre-index()
    (load_series(path="data_raw/harmonic.txt") + load_series(generator="gauss")).to_csv(
        "data_raw/gauss_additiv.txt", header=None, index=False
    )


if __name__ == "__main__":
    app.run()
