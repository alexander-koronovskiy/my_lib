import os

from flask import Flask, render_template, request

from calc.aggregator import load_series
from calc.transform import process
from calc.resulting import build_cd_dfa_graphics, build_dfa_graphics

app = Flask(__name__)
ORIG_DATA = "filtered_data"
ORIG_IMG_SCALE = 5500, 6000


@app.route("/")
def index():
    time_series = os.listdir(ORIG_DATA)
    return render_template(
        "index.html", time_series=time_series, title="Extended DFA transform"
    )


@app.route("/graphics")
def result():
    path = request.args.get("jsdata")
    build_dfa_graphics(ORIG_DATA, path, ORIG_IMG_SCALE)
    images = os.listdir("static/images")
    return render_template("graphics.html", images=reversed(images))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


def save_ts(upload_dir, file_name):  # pre-index()
    process(function="filtering",
            df=load_series(path="pure_data/linear.txt"))\
        .to_csv(f"{upload_dir}/{file_name}", header=None, index=False)


if __name__ == "__main__":
    app.run()
