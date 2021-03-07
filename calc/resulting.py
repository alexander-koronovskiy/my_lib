import os

import matplotlib.pyplot as plt
import seaborn as sns


def df_handler(df):

    # validation
    if df["profile"].empty or df["dfa_transform"].empty:
        raise KeyError("You transmit incomplete dataframe")

    # routing files
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = base_dir + "/dataframes/dataframe.csv"
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
