import os

from flask import Flask, render_template, request

from calc.aggregator import load_series
from calc.resulting import build_cd_dfa_graphics, build_dfa_graphics

app = Flask(__name__)
ORIG_DATA = "pure_data"


@app.route("/")
def index():
    time_series = os.listdir(ORIG_DATA)
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


def save_ts(upload_dir, file_name):  # pre-index()
    (load_series(generator="linear"))\
        .to_csv(f"{upload_dir}/{file_name}", header=None, index=False)


if __name__ == "__main__":
    app.run()
