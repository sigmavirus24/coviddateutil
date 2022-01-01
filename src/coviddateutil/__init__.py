"""Package for calculating the current COVID date."""
import datetime
import typing as t

import attrs

__version__ = "2020.03.670"

__all__ = (
    "coviddate",
    "today",
    "usingdate",
)


_START_OF_COVID = datetime.date(2020, 3, 1)

_MONTHS = [
    "_offset",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def _utcnow() -> datetime.datetime:
    return datetime.datetime.now(datetime.timezone.utc)


def _utctoday() -> datetime.date:
    return _utcnow().date()


cd = t.TypeVar("cd", bound="coviddate")


@attrs.frozen
class coviddate:  # noqa: N801
    """Do the heavy lifting of figuring out today's date."""

    year: int = attrs.field()
    month: int = attrs.field()
    day: int = attrs.field()

    _refdate: datetime.date = attrs.field(
        validator=attrs.validators.instance_of(datetime.date),
    )

    @classmethod
    def from_datetime(cls: t.Type[cd], dt: datetime.datetime) -> cd:
        """Create a coviddate from a datetime object."""
        return cls.from_date(dt.date())

    @classmethod
    def from_date(cls: t.Type[cd], dt: datetime.date) -> cd:
        """Create a coviddate from a date object."""
        year = 2020
        month = 3
        day = 1

        if dt.year < 2020:
            year = dt.year
            month = dt.month
            day = dt.day

        elif dt.year == 2020:
            if dt.month <= 3:
                month = dt.month
                day = dt.day

        else:
            diff: datetime.timedelta = dt - _START_OF_COVID
            day = diff.days

        return cls(year, month, day, refdate=dt)

    def __repr__(self) -> str:  # noqa: D105
        return f"{_MONTHS[self.month]} {self.day}, {self.year}"


def today() -> coviddate:
    """Create a coviddate object with today's date object."""
    return coviddate.from_date(_utctoday())


def usingdate(date: datetime.date) -> coviddate:
    """Create a coviddate object from a pre-defined date object."""
    return coviddate.from_date(date)
