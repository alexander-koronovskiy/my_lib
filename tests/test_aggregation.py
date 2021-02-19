import os

from app.aggregator import load_series
from app.data_gen import f_u, f_v, f_w, f_x, f_y, f_z


def test_existing_raw_file_aggregation():
    """
    test checking that the non-existing raw file is correctly handled
    """
    neph_data_df = load_series(
        path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        + "/app/data_raw/close_mod.txt"
    )
    neph_data_df.columns = ["u"]
    assert len(neph_data_df.columns) > 1


def test_diff_solution_seq_handle_correctly():
    """
    test checking that sequence is aggregated correctly
    """
    diff_solution_df = load_series(
        generator="diff_sol",
        t=[1, 1, 1, 0.1, 0.1, 0.1],
        f=[f_x, f_y, f_z, f_u, f_v, f_w],
    )
    diff_solution_df.columns = ["t", "x", "y", "z", "u", "v", "w"]
    assert len(diff_solution_df.columns) > 1


# add tests for another sequences
