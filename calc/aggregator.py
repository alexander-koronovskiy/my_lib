"""
Aggregation raw data or sequence to 1-d: [u] or more-d: [t, u0..ux] time series
in pandas DataFrame format

linear, nonlinear, harmonic and solution of differential equation sequence are agg.
"""

from calc.data_gen import base_noise, diff_sol, harmonic, linear, nonlinear, pd

SERIES = {
    "linear": linear,
    "nonlinear": nonlinear,
    "harmonic": harmonic,
    "diff_sol": diff_sol,
    "white_noise": base_noise,
}


def load_series(path=None, generator=None, **kwargs):
    """
    2-x column [x, y] series generator from file path or function
    from module series use aggregator.load_series()

    :param path: loading series from file
    :param generator: function generator call
    :param kwargs: function :params call
    :return: pandas DataFrame in [x, y] format
    """
    if generator is not None:
        # generation
        if isinstance(generator, str):
            # get generator function and call it
            f = SERIES.get(generator)
            if f is None:
                raise RuntimeError(f"No such generator: {generator}")
            return f(**kwargs)
        elif callable(generator):
            # call generator
            return generator(**kwargs)
        else:
            raise RuntimeError(
                f"This type of generator is not supported: {type(generator)}"
            )
    elif path is not None:
        with open(path) as file:
            data = pd.DataFrame([line.split() for line in file], dtype="float64")
            if len(data.columns) == 1:
                data.columns = ["u"]
        return data
    else:
        raise RuntimeError("You should set either path or generator!")
