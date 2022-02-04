"""
tests check that generated and sequence from file
is aggregated to dataframe format correctly
"""

import os

from calc.aggregator import load_series
from calc.data_gen import f_u, f_v, f_w, f_x, f_y, f_z

file_path = (
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    + "/pure_data/close_mod.txt"
)


def test_existing_raw_file_aggregation():
    assert not load_series(path=file_path).empty


def test_diff_solution_seq_handle_correctly():
    diff_solution_df = load_series(
        generator="diff_sol",
        t=[1, 1, 1, 0.1, 0.1, 0.1],
        f=[f_x, f_y, f_z, f_u, f_v, f_w],
    )
    diff_solution_df.columns = ["t", "x", "y", "z", "u", "v", "w"]

    # saving
    file_path_2 = (
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        + "/pure_data/diff_sol.txt"
    )
    diff_solution_df["u"].to_csv(file_path_2, index=False, header=None)

    assert not diff_solution_df.empty


def test_data_create():
    component_first_df = load_series(generator="harmonic", points=10000)
    component_second_df = load_series(generator="white_noise", points=10000)
    signal_df = component_first_df["u"] + component_second_df["u"]

    # saving
    file_path_3 = (
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        + "/pure_data/gauss_additiv.txt"
    )
    signal_df.to_csv(file_path_3, index=False, header=None)

    assert not signal_df.empty
