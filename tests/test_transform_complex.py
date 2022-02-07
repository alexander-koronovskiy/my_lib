"""
tests for complex operation with dataframes works correctly
"""

import os

from calc.aggregator import load_series
from calc.transform import process

file_path = (
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    + "/pure_data/close_mod.txt"
)


def test_approximation():
    df = load_series(path=file_path)
    df = process(function="approx", df=df)
    assert not df["approx"].empty


def test_akf():
    lags_points = 10
    df = load_series(generator="harmonic")
    df = process(function="akf", df=df, lags=lags_points)
    assert not df["akf"].empty


def test_dfa_many():
    df = load_series(path=file_path)
    df = process(function="profile", df=df)
    df = process(function="dfa_extended", df=df)
    assert not df["dfa_lags"].empty
    assert not df["dfa_transform"].empty
    assert not df["dfa_ext_transform"].empty


def test_dfa_points():
    df = load_series(path=file_path)
    df = process(function="profile", df=df)
    df = process(function="dfa_extended", df=df)
    assert (
        len(df["dfa_lags"]) == len(df["dfa_transform"]) == len(df["dfa_ext_transform"])
    )
