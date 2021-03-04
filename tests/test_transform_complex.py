"""
tests for complex operation with dataframes works correctly
"""

import os

from app.aggregator import load_series
from app.transform import process

file_path = (
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    + "/data_raw/close_mod.txt"
)


def test_approximation():
    df = load_series(path=file_path)
    df = process(function="approx", df=df)
    assert not df["approx"].empty


def test_akf():
    lags_points = 10
    df = load_series(generator="harmonic")
    df = process(function="akf", df=df, lags=lags_points)
    assert len(df["akf"]) == lags_points


def test_dfa_many():
    df = load_series(path=file_path)
    df = process(function="approx", df=df)
    assert False
