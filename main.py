#!/usr/bin/env python3
from datetime import date, datetime
from enum import IntEnum


START_COUNTER: int = 1
START_DATE: date = date(2019, 1, 1)  # Tuesday January 01 2019
DAYS_IN_WEEK: int = 7


class SmallDateException(Exception):
    pass


class OffsetDay(IntEnum):
    MONDAY = 6
    TUESDAY = 5
    WEDNESDAY = 4
    THURSDAY = 3
    FRIDAY = 2
    SATURDAY = 1
    SUNDAY = 0


def _get_offset_by_start_date() -> int:
    start_week_day = START_DATE.weekday()

    for i, value in enumerate(OffsetDay):
        if i == start_week_day:
            return value.value


def get_week_number_by_date(input_date: date) -> int:
    """
    Defines the week number by the input date.
    Week starts from Sunday.
    """

    if input_date < START_DATE:
        raise SmallDateException(f"input_date is less than START_DATE = {START_DATE}")

    if input_date == START_DATE:
        return START_COUNTER

    # Get timedelta between two dates
    delta = input_date - START_DATE
    # Get day number of week
    week_day = input_date.weekday()
    # Get week number. Consider START_DATE is Monday and week starts from Monday.
    count = (delta.days // DAYS_IN_WEEK) + START_COUNTER

    # Corrective. START_DATE can be Monday and week starts from Sunday.
    remainder = delta.days % DAYS_IN_WEEK
    offset = _get_offset_by_start_date()
    if remainder >= offset:
        count += 1

    return count
