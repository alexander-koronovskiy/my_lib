"""
tests for base operation with dataframes works correctly
"""

import os

from app.aggregator import load_series
from app.transform import process


def test_addiction():
    df1 = load_series(generator="linear")
    df2 = load_series(generator="harmonic")
    df = process(
        function="addiction", df_first=df1, df_second=df2, first_col="u", second_col="u"
    )
    assert df.columns == ["w"]


def test_multiply():
    df1 = load_series(generator="linear")
    df2 = load_series(generator="harmonic")
    df = process(
        function="multiply", df_first=df1, df_second=df2, first_col="u", second_col="u"
    )
    assert df.columns == ["w"]


def test_integrate():
    file_path = (
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        + "/data_raw/close_mod.txt"
    )
    df = load_series(path=file_path)
    df.columns = ["u"]
    df = process(function="integrate", df=df)
    assert not df["integrate"].empty


def test_profile():
    file_path = (
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        + "/data_raw/close_mod.txt"
    )
    df = load_series(path=file_path)
    df.columns = ["u"]
    df = process(function="profile", df=df)
    assert not df["profile"].empty
