import os

from calc.aggregator import load_series
from calc.resulting import df_handler
from calc.transform import process

abs_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_dir = abs_path + "/dataframes"
img_dir = abs_path + "/static/images"


def test_valid_df_handle():
    df = load_series(path=abs_path + "/data_raw/close_mod.txt")
    df = process(function="profile", df=df)
    df = process(function="dfa_extended", df=df)
    df_handler(df)
    assert os.listdir(csv_dir)
    assert len(os.listdir(img_dir)) == 5


def test_clear_after_app_worked():
    pass
