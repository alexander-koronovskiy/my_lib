"""
pandas DataFrame processing methods

integration, series profile(integration without mean),
approximation, auto-correlation function, correlation function,
detrending fluctuation analysis of multifractal time series,
fourier analysis, synchronisation phases building
compare graphs, 3d-graphs, df results save
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.font_manager import FontProperties
from pylab import figure, grid, legend, plot, savefig, title, xlabel


def integrate(df, input_col="u", output_col="integrate"):
    """
    integration time series method
    use "function='integrate', :params" in () process

    :param df: DataFrame with time series for integration
    :param input_col: time series column for integration
    :param output_col: integrated time series column
    :return: DataFrame with integrated time series column
    """
    df[output_col] = df[input_col].cumsum()
    return df


def compute_profile(df, input_col="u", output_col="profile"):
    """
    integration without mean time series method
    use "function='compute_profile', :params" in () process

    :param df: DataFrame with time series for integration without mean
    :param input_col: time series column for integration without mean
    :param output_col: integrated time series column without mean
    :return: DataFrame with integrated without mean time series column
    """
    df[output_col] = (df[input_col] - df[input_col].mean()).cumsum()
    return df


def approx(df, n=1, input_col="u", output_col="approx"):
    """
    approximation time series method
    use "function='approx', :params" in () process

    :param df: DataFrame with time series for approximation
    :param n: order of approximation
    :param input_col: time series column for approximation
    :param output_col: approximated time series column
    :return: DataFrame with approximated time series column
    """
    t = np.linspace(0, 10, len(df[input_col]))
    p = np.polyfit(t, df[input_col], n)
    df[output_col] = np.polyval(p, t)
    return df


def akf(df, lags=15, input_col="u", output_col="akf"):
    """
    auto-correlation function
    use "function='akf', :params" in () process

    :param df: DataFrame with time series for auto-correlation function build
    :param lags: precision for auto-correlation function build; lags < time series length
    :param input_col: time series column for auto-correlation function build
    :param output_col: auto-correlation function series
    :return: DataFrame with auto-correlation function series
    """
    corr = [
        1.0 if l == 0 else np.corrcoef(df[input_col][l:], df[input_col][:-l])[0][1]
        for l in range(lags)
    ]
    df = df.combine_first(pd.DataFrame(corr, columns=[output_col]))
    return df


def dfa1(
    df,
    input_col="u",
    q=1,
    l_lags=[5, 10, 20, 50, 100, 200],
    lags_col="output_lags",
    dfa_col="output_dfa",
    ext_col="output_dfa_ext",
):
    """
    De-trending fluctuation analysis - is one of the nonlinear dynamics methods
    for time series correlation analysis

    :param df: DataFrame with integrated without mean function, named as "profile"
    :param input_col: time series prepared for dfa-processing
    :param q: approximation order for dfa-processing
    :param l_lags: parts for dividing time series
    :param lags_col: "time window" sizes in log10 scale
    :param dfa_col: result function value in log10 scale
    :return: DataFrames with built dfa
    """
    f_res = []
    ext_df = []

    for i in l_lags:
        # chunk the column
        chunks = np.array_split(df[input_col], i)

        # approximation chunks;
        t = [np.linspace(0.1, 10, len(chunks[j])) for j in range(len(chunks))]
        p = [np.polyfit(t[j], chunks[j], q) for j in range(len(t))]
        approx_chunks = [np.polyval(p[j], t[j]) for j in range(len(t))]

        # another way standard dfa
        # sum([sum(np.sqrt((approx_chunks[i] - chunks[i]) ** 2)) / len(approx_chunks[i])
        # for i in range(len(approx_chunks))]) / len(approx_chunks)

        ext_df.append(
            max(
                [
                    sum(np.sqrt((approx_chunks[i] - chunks[i]) ** 2))
                    / len(approx_chunks[i])
                    for i in range(len(approx_chunks))
                ]
            )
            - min(
                [
                    sum(np.sqrt((approx_chunks[i] - chunks[i]) ** 2))
                    / len(approx_chunks[i])
                    for i in range(len(approx_chunks))
                ]
            )
        )

        # de-trending
        approx = []
        for lst in approx_chunks:
            approx.extend(lst)
        f_res.append(
            sum(np.sqrt((df[input_col] - np.array(approx)) ** 2)) / len(df[input_col])
        )

    df[lags_col] = pd.DataFrame(np.log10(np.array(len(df[input_col])) / l_lags))
    df[dfa_col] = pd.DataFrame(np.log10(f_res))
    df[ext_col] = pd.DataFrame(np.log10(ext_df))

    return df


def sync_phase():
    pass


def fourier():
    pass


def series_fig(df, name="input_signal"):
    """
    saving input series and profile

    :param df: DataFrame
    :param name: path name or input series type
    :return: series and profile png graphics
    """
    f, a = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    a[0].set_title("series")
    a[1].set_title("profile")
    a[0].plot(df["u"])
    a[1].plot(df["profile"])
    plt.savefig(name, dpi=100)
    plt.clf()


def save_dfa_graphics(df, st_dfa, ext_dfa, name="dfa_graphics"):
    """
    saving standard and extended DFA-function results

    :param df: DataFrame of DFA analysis result
    :param name: path name or input series type
    :return: png graphics of DFA results
    """
    plt.plot(df["output_lags"], df["dfa_1"])
    plt.plot(df["output_lags"], df["dfa_ext_1"])
    figure(1, figsize=(10, 8))
    plt.xlabel(r"$lg L$")
    plt.ylabel(r"$lg F, lg dF$")
    grid(True)
    legend(
        (r"$alpha$: " + str(st_dfa), r"$betta$: " + str(ext_dfa)),
        prop=FontProperties(size=16),
    )
    plt.savefig(name, dpi=100)
    plt.clf()


FUNCTIONS = {
    "integrate": integrate,
    "compute_profile": compute_profile,
    "approx": approx,
    "akf": akf,
    "dfa1": dfa1,
    "sync_phase": sync_phase,
    "fourier": fourier,
    "save_dfa_graphics": save_dfa_graphics,
    "series_fig": series_fig,
}


def process(function=None, **kwargs):
    """
    series handler
    from module series use series.load_series()

    :param function: processing function call
    :param kwargs: function :params call
    :return: pandas DataFrame processed by :function
    """
    if function is not None:
        # handler
        if isinstance(function, str):
            # get handler function and call it
            f = FUNCTIONS.get(function)
            if f is None:
                raise RuntimeError(f"No such generator: {function}")
            return f(**kwargs)
        elif callable(function):
            # call handler
            return function(**kwargs)
        else:
            raise RuntimeError(
                f"This type of generator is not supported: {type(function)}"
            )
    else:
        raise RuntimeError("You should set handler!")
