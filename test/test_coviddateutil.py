import datetime

import pytest

import coviddateutil


def test_today() -> None:
    today = coviddateutil.today()
    assert today.month == 3
    assert today.year == 2020
    assert today.day >= 670


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            datetime.date(2020, 1, 20),
            coviddateutil.coviddate(2020, 1, 20, datetime.date(2020, 1, 20)),
        ),
        (
            datetime.date(2020, 3, 1),
            coviddateutil.coviddate(2020, 3, 1, datetime.date(2020, 3, 1)),
        ),
        (
            datetime.date(2020, 3, 10),
            coviddateutil.coviddate(2020, 3, 10, datetime.date(2020, 3, 10)),
        ),
        (
            datetime.date(2021, 3, 10),
            coviddateutil.coviddate(2020, 3, 374, datetime.date(2021, 3, 10)),
        ),
        (
            datetime.date(2021, 12, 31),
            coviddateutil.coviddate(2020, 3, 670, datetime.date(2021, 12, 31)),
        ),
    ],
)
def test_usingdate(input, expected) -> None:
    day = coviddateutil.usingdate(input)
    assert day == expected
