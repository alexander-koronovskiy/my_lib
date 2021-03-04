"""
tests check that generated and sequence from file
is aggregated to dataframe format correctly
"""

import os

from app.aggregator import load_series
from app.data_gen import f_u, f_v, f_w, f_x, f_y, f_z


def test_existing_raw_file_aggregation():
    file_path = (
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        + "/data_raw/close_mod.txt"
    )
    neph_data_df = load_series(path=file_path)
    neph_data_df.columns = ["u"]
    assert not neph_data_df.empty


def test_diff_solution_seq_handle_correctly():
    diff_solution_df = load_series(
        generator="diff_sol",
        t=[1, 1, 1, 0.1, 0.1, 0.1],
        f=[f_x, f_y, f_z, f_u, f_v, f_w],
    )
    diff_solution_df.columns = ["t", "x", "y", "z", "u", "v", "w"]
    assert not diff_solution_df.empty
