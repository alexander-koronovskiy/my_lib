import os

from flask import Flask, render_template, request

from calc.aggregator import load_series
from calc.data_gen import f_u, f_v, f_w, f_x, f_y, f_z
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
    diff_ts = (
        load_series(
            generator="diff_sol",
            t=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
            f=[f_x, f_y, f_z, f_u, f_v, f_w],
        )[4]
        + load_series(generator="gauss")["u"]
    )
    diff_ts.to_csv("data_raw/gauss_additiv.txt", header=None, index=False)


if __name__ == "__main__":
    save_ts()
