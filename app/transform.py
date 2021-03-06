"""
complex results built by 2 coordinates usually: output values and lags
complex results may contains more than one output values column
"""

import numpy as np
import pandas as pd


def addiction(df_first, df_second, first_col, second_col, output_col="u"):
    """
    integration time series method
    use "function='addiction', :params" in () process

    df_first: first dataframe
    df_second: second dataframe
    first_col: first col in 1 dataframe
    second_col: second col in 2nd dataframe

    create the new dataframe - df
    result put in the output column
    """
    df = pd.DataFrame()
    df[output_col] = df_first[first_col] + df_second[second_col]
    return df


def multiply(df_first, df_second, first_col, second_col, output_col="u"):
    """
    integration time series method
    use "function='addiction', :params" in () process

    df_first: first dataframe
    df_second: second dataframe
    first_col: first col in 1 dataframe
    second_col: second col in 2nd dataframe

    create the new dataframe - df
    result put in the output column
    """
    df = pd.DataFrame()
    df[output_col] = df_first[first_col] * df_second[second_col]
    return df


def integrate(df, input_col="u", output_col="integrate"):
    """
    integration time series method
    use "function='integrate', :params" in () process

    df: DataFrame with time series for integration
    input_col: time series column for integration
    output_col: integrated time series column
    """
    df[output_col] = df[input_col].cumsum()
    return df


def compute_profile(df, input_col="u", output_col="profile"):
    """
    integration without mean time series method
    use "function='compute_profile', :params" in () process

    df: DataFrame with time series for integration without mean
    input_col: time series column for integration without mean
    output_col: integrated time series column without mean
    """
    df[output_col] = (df[input_col] - df[input_col].mean()).cumsum()
    return df


def approx(df, n=1, input_col="u", output_col="approx"):
    """
    approximation time series method
    use "function='approx', :params" in () process

    df: DataFrame with time series for approximation
    n: order of approximation
    input_col: time series column for approximation
    output_col: approximated time series column
    """
    t = np.linspace(0, 10, len(df[input_col]))
    p = np.polyfit(t, df[input_col], n)
    df[output_col] = np.polyval(p, t)
    return df


def akf(df, lags=15, input_col="u", output_col="akf"):
    """
    auto-correlation function
    use "function='akf', :params" in () process

    df: DataFrame with time series for auto-correlation function build
    lags: precision for auto-correlation function build; lags < time series length
    input_col: time series column for auto-correlation function build
    output_col: auto-correlation function series
    """
    corr = [
        1.0 if l == 0 else np.corrcoef(df[input_col][l:], df[input_col][:-l])[0][1]
        for l in range(lags)
    ]
    df = df.combine_first(pd.DataFrame(corr, columns=[output_col]))
    return df


def dfa_extended(
    df,
    input_col="profile",
    q=1,
    l_lags=(5, 10, 20, 50, 100, 200),
    lags_col="dfa_lags",
    dfa_col="dfa_transform",
    ext_col="dfa_ext_transform",
):
    """
    De-trending fluctuation analysis - is one of the nonlinear dynamics methods
    for time series correlation analysis

    df: DataFrame with integrated without mean function, named as "profile"
    input_col: time series prepared for dfa-processing
    q: approximation order for dfa-processing
    l_lags: parts for dividing time series
    lags_col: "time window" sizes in log10 scale
    dfa_col: result function value in log10 scale
    """
    f_res = []
    ext_df = []

    for i in l_lags:

        # chunks the column
        chunks = np.array_split(df[input_col], i)

        # approximation chunks;
        t = [np.linspace(0.1, 10, len(chunks[j])) for j in range(len(chunks))]
        p = [np.polyfit(t[j], chunks[j], q) for j in range(len(t))]
        approx_chunks = [np.polyval(p[j], t[j]) for j in range(len(t))]

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

    # saving result
    df[lags_col] = pd.DataFrame(np.log10(np.array(len(df[input_col])) / l_lags))
    df[dfa_col] = pd.DataFrame(np.log10(f_res))
    df[ext_col] = pd.DataFrame(np.log10(ext_df))

    return df


FUNCTIONS = {
    "addiction": addiction,
    "multiply": multiply,
    "integrate": integrate,
    "profile": compute_profile,
    "approx": approx,
    "akf": akf,
    "dfa_extended": dfa_extended,
}


def process(function=None, **kwargs):
    """
    series handler
    from module series use series.load_series()

    function: processing function call
    kwargs: function :params call
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
