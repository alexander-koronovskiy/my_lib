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


def del_old_files(dir) -> None:
    curdir = base_dir + dir
    filelist = [f for f in os.listdir(curdir)]
    for f in filelist:
        os.remove(os.path.join(curdir, f))


def build_dfa_graphics(path) -> None:
    """
    web-interface supporting method
    it contains all the step for DFA-transform building
    and saves processing result

    saves graphics of profile, time series
    alpha and betta coefficient dependence
    """
    del_old_files("/static/images")
    del_old_files("/dataframes")

    # dfa building
    df = load_series(path=base_dir + "/data_raw/" + path)
    df = process(function="profile", df=df)
    df = process(function="dfa_extended", df=df)

    # routing files
    csv_path = base_dir + "/dataframes/dataframe.csv"
    orig_img_path = base_dir + "/static/images/orig.png"
    profile_img_path = base_dir + "/static/images/profile.png"
    dfa_img_path = base_dir + "/static/images/dfa.png"
    dfa_ext_img_path = base_dir + "/static/images/dfa_ext.png"
    dfa_many_img_path = base_dir + "/static/images/dfa_many.png"

    # saving results
    df.to_csv(csv_path, index=False)
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


def build_cd_dfa_graphics(path):
    """
    new algorithm - cd dfa build
    """
    del_old_files("/static/images")
    del_old_files("/dataframes")

    # time series and cD coefficient obtaining
    df = load_series(path=base_dir + "/data_raw/" + path)
    order = "db8"
    cA, cD = pywt.dwt(df, order)
    cd_df = pd.DataFrame({"u": cD.transpose()[-1]})

    # dfa building
    df = process(function="profile", df=df)
    df = process(function="dfa_extended", df=df)
    cd_df = process(function="profile", df=cd_df)
    cd_df = process(function="dfa_extended", df=cd_df)

    # routing files
    orig_img_path = base_dir + "/static/images/time_series.png"
    cd_img_path = base_dir + "/static/images/cD.png"
    cd_dfa_img_path = base_dir + "/static/images/DFA_cD.png"
    ts_path = base_dir + "/dataframes/time_series.csv"
    cd_path = base_dir + "/dataframes/cD.csv"

    # saving results
    df.to_csv(ts_path, index=False)
    cd_df.to_csv(cd_path, index=False)
    sns.lineplot(data=df["u"]).get_figure().savefig(orig_img_path)
    plt.clf()
    sns.lineplot(data=cd_df["u"]).get_figure().savefig(cd_img_path)
    plt.clf()
    sns.lineplot(x=cd_df["dfa_lags"], y=cd_df["dfa_transform"]).get_figure().savefig(
        cd_dfa_img_path
    )
    plt.clf()
