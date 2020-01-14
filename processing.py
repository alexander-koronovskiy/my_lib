"""
pandas DataFrame processing methods

integration, series profile(integration without mean),
approximation, auto-correlation function, correlation function,
detrending fluctuation analysis of multifractal time series,
fourier analysis, synchronisation phases building
compare graphs, 3d-graphs, df results save
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def integrate(df, input_col='u', output_col='integrate'):
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


def compute_profile(df, input_col='u', output_col='profile'):
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


def approx(df, n=1, input_col='u', output_col='approx'):
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


def akf(df, lags=15, input_col='u', output_col='akf'):
    """
    auto-correlation function
    use "function='akf', :params" in () process

    :param df: DataFrame with time series for auto-correlation function build
    :param lags: precision for auto-correlation function build; lags < time series length
    :param input_col: time series column for auto-correlation function build
    :param output_col: auto-correlation function series
    :return: DataFrame with auto-correlation function series
    """
    corr = [1. if l == 0 else np.corrcoef(df[input_col][l:], df[input_col][:-l])[0][1] for l in range(lags)]
    df = df.combine_first(pd.DataFrame(corr, columns=[output_col]))
    return df


def dfa1(df, input_col='u', n=1, l_lags=[5, 10, 20, 50, 100, 200], lags_col='output_lags', dfa_col='output_res'):
    f_res = []
    for i in l_lags:
        # chunk the column
        chuncks = np.array_split(df[input_col], i)

        # approximation chunks; if n < 0 df[input_col]**(-1) ??
        t = [np.linspace(0.1, 10, len(chuncks[j])) for j in range(len(chuncks))]
        p = [np.polyfit(t[j], chuncks[j], n) for j in range(len(t))]
        approx_chunks = [np.polyval(p[j], t[j]) for j in range(len(t))]

        # detrending
        approx = []
        for lst in approx_chunks:
            approx.extend(lst)
        f_res.append(sum(np.sqrt((df[input_col] - np.array(approx))**2))/len(df[input_col]))

    dfa_l = pd.DataFrame(np.log2(np.array(len(df[input_col])) / l_lags), columns=['dfa_lags'])
    dfa_r = pd.DataFrame(np.log2(f_res), columns=['dfa_res'])
    df[lags_col] = dfa_l
    df[dfa_col] = dfa_r
    return df


def dfa3():
    pass


def sync_phase():
    pass


def fourier():
    pass


def compare_graphics(df, orig_col, profile_col, dfa_l_col, dfa_f_col, title1='in', title2='out'):
    """
    two graphics compare method
    use "function='compare_graphics', :params" in () process

    :param df: DataFrame with considered time series
    :param orig_col: initial time series from file or gen function
    :param profile_col: computed profile for init time series
    :param dfa_l_col: lg2 time window for dfa graphics
    :param dfa_l_col: lg2 dfa function value for dfa graphics
    :param title1: first graphic title
    :param title2: second graphic title
    :return: a two graphics in one figure
    """
    f, a = plt.subplots(1, 3, figsize=(12, 4))
    a[0].plot(df[profile_col])

    a[1].plot(df[[orig_col]])
    a[1].set_title(title1)

    a[2].plot(df[dfa_l_col], df[dfa_f_col])
    a[2].set_title(title2)
    plt.show()


FUNCTIONS = {
    'integrate': integrate,
    'compute_profile': compute_profile,
    'approx': approx,
    'akf': akf,
    'dfa1': dfa1,
    'dfa3': dfa3,
    'sync_phase': sync_phase,
    'fourier': fourier,
    'compare_graphics': compare_graphics,
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
                raise RuntimeError(f'No such generator: {function}')
            return f(**kwargs)
        elif callable(function):
            # call handler
            return function(**kwargs)
        else:
            raise RuntimeError(f'This type of generator is not supported: {type(function)}')
    else:
        raise RuntimeError('You should set handler!')
