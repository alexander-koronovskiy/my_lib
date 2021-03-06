"""
tests for base operation with dataframes works correctly
"""

import os

from calc.aggregator import load_series
from calc.transform import process

file_path = (
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    + "/data_raw/close_mod.txt"
)


def test_addiction():
    df1 = load_series(generator="linear")
    df2 = load_series(generator="harmonic")
    df = process(
        function="addiction", df_first=df1, df_second=df2, first_col="u", second_col="u"
    )
    assert df.columns == ["u"]


def test_multiply():
    df1 = load_series(generator="linear")
    df2 = load_series(generator="harmonic")
    df = process(
        function="multiply", df_first=df1, df_second=df2, first_col="u", second_col="u"
    )
    assert df.columns == ["u"]


def test_integrate():
    df = load_series(path=file_path)
    df = process(function="integrate", df=df)
    assert not df["integrate"].empty


def test_profile():
    df = load_series(path=file_path)
    df = process(function="profile", df=df)
    assert not df["profile"].empty
