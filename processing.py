"""
pandas DataFrame processing methods

integration, series profile(integration without mean),
approximation, auto-correlation function,
detrending fluctuation analysis of multifractal time series,
fourier analysis, synchronisation phases building
compare graphs, 3d-graphs, df results save
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def integrate(df, input_col='u', output_col='profile_u'):
    """
    integration time series method
    use "function=integrate, :params" in () process

    :param df: DataFrame with time series for integration
    :param input_col: time series column for integration
    :param output_col: integrated time series column
    :return: DataFrame with integrated time series column
    """
    df[output_col] = df[input_col].cumsum()
    return df


def compute_profile(df, input_col='u', output_col='profile_u'):
    """
    integration without mean time series method
    use "function=compute_profile, :params" in () process

    :param df: DataFrame with time series for integration without mean
    :param input_col: time series column for integration without mean
    :param output_col: integrated time series column without mean
    :return: DataFrame with integrated without mean time series column
    """
    df[output_col] = (df[input_col] - df[input_col].mean()).cumsum()
    return df


def approx(df, n=1, input_col='u', output_col='approx_u'):
    """
    approximation time series method
    use "function=approx, :params" in () process

    :param df: DataFrame with time series for approximation
    :param n: order of approximation
    :param input_col: time series column for approximation
    :param output_col: approximated time series column
    :return: DataFrame with approximated time series column
    """
    t = np.linspace(0.1, 10, len(df[input_col]))
    p = np.polyfit(t, df[input_col], n)
    df[output_col] = np.polyval(p, t)
    return df


def akf(df, lags=15, input_col='u', output_col='akf_u'):
    """
    auto-correlation function
    use "function=akf, :params" in () process

    :param df: DataFrame with time series for auto-correlation function build
    :param lags: precision for auto-correlation function build; lags < time series length
    :param input_col: time series column for auto-correlation function build
    :param output_col: auto-correlation function series
    :return: DataFrame with auto-correlation function series
    """
    corr = [1. if l == 0 else np.corrcoef(df[input_col][l:], df[input_col][:-l])[0][1] for l in range(lags)]
    df = df.combine_first(pd.DataFrame(corr, columns=[output_col]))
    return df


def dfa1():
    pass


def dfa3():
    pass


def sync_phase():
    pass


def fourier():
    pass


def compare_graphs(df, first_col, second_col, title1='in', title2='out'):
    """
    two graphics compare method
    use "function=compare_graphs, :params" in () process

    :param df: DataFrame with considered time series
    :param first_col: first time series
    :param second_col: second time series, for example - processed by func
    :param title1: first graphic title
    :param title2: second graphic title
    :return: a two graphics in one figure
    """
    f, a = plt.subplots(1, 2)
    a[0].plot(df[first_col])
    a[0].set_title(title1)
    a[1].plot(df[second_col])
    a[1].set_title(title2)
    plt.show()


FUNCTIONS = {
    'integrate': integrate,
    'profile': compute_profile,
    'approx': approx,
    'akf': akf,
    'dfa1': dfa1,
    'dfa3': dfa3,
    'sync_phase': sync_phase,
    'fourier': fourier,
    'compare_graphs': compare_graphs,
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
