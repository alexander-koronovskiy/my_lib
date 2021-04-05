"""
methods for final calculating result for web-interface
step for DFA-transform building
- forming text data
- transform data from path to dataframe
- pre-processing like slicing (optional)
- profile building
- DFA transform building
- post-processing approximate the resulting curve
- saving result
"""
import os

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import pywt
import seaborn as sns

from calc.aggregator import load_series
from calc.transform import process

matplotlib.use("Agg")


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def build_dfa_graphics(path) -> None:
    """
    web-interface supporting method
    it contains all the step for DFA-transform building
    and saves processing result

    saves graphics of profile, time series
    alpha and betta coefficient dependence
    """
    # df building
    df = load_series(path=base_dir + "/data_raw/" + path)
    df = process(function="profile", df=df)
    df = process(function="dfa_extended", df=df)

    # routing files
    csv_path = base_dir + "/dataframe.csv"
    orig_img_path = base_dir + "/static/images/orig.png"
    profile_img_path = base_dir + "/static/images/profile.png"
    dfa_img_path = base_dir + "/static/images/dfa.png"
    dfa_ext_img_path = base_dir + "/static/images/dfa_ext.png"
    dfa_many_img_path = base_dir + "/static/images/dfa_many.png"

    # save df to csv
    df.to_csv(csv_path, index=False)  # header=none

    # saving images
    sns.lineplot(data=df["u"]).get_figure().savefig(orig_img_path)
    plt.clf()
    sns.lineplot(data=df["profile"]).get_figure().savefig(profile_img_path)
    plt.clf()
    sns.lineplot(x=df["dfa_lags"], y=df["dfa_ext_transform"]).get_figure().savefig(
        dfa_ext_img_path
    )
    plt.clf()
    sns.lineplot(x=df["dfa_lags"], y=df["dfa_transform"]).get_figure().savefig(
        dfa_img_path
    )
    sns.lineplot(x=df["dfa_lags"], y=df["dfa_ext_transform"]).get_figure().savefig(
        dfa_many_img_path
    )
    plt.clf()


def build_dwt_dfa_graphics(path):
    """
    new algorithm
    """

    # load series
    x = load_series(path=base_dir + "/data_raw/" + path)

    # dwt
    order = "db2"
    cA, cD = pywt.dwt(x, order)
    u = cA.transpose()[0]
    df = pd.DataFrame(data={"u": u})

    # routing files
    # save df to csv
    # saving images to
    # 1-2.time_series, profile
    # 3-4.cA, cD graphics
    # 5-6.DFA cA, DFA cD
