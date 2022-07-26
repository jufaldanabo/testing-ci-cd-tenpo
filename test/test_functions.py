from functions import add_two_numbers, Cleaning
import pandas as pd
import pytest


def test_add_two_numbers():
    assert (add_two_numbers(1, 2)) == 6
    assert (add_two_numbers(-1, 2)) == 1


@pytest.fixture()
def data_raw():
    return Cleaning(
        df=pd.DataFrame({"identificacion": [1, 2, 3, 4, 5555555, 66666]}),
        variable="identificacion",
    )


def test_remmove_invalid_id(data_raw):
    assert data_raw.remmove_invalid_id().shape == (4, 1)
