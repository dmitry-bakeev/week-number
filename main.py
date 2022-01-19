#!/usr/bin/env python3
import json

from datetime import date, datetime
from enum import IntEnum


START_COUNTER: int = 1
START_DATE: date = date(2019, 1, 1)  # Tuesday January 01 2019
DAYS_IN_WEEK: int = 7
DATE_FORMAT: str = '%Y-%m-%d'
NEED_DATE_MSG: str = 'Need GET parameter date. Format is YYYY-MM-DD. Example ?date=2019-01-01'


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


def parse_date(input_date_str: str) -> date:
    return datetime.strptime(input_date_str, DATE_FORMAT).date()


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

    # Corrective. START_DATE can be not Monday and week starts from Sunday.
    remainder = delta.days % DAYS_IN_WEEK
    offset = _get_offset_by_start_date()
    if remainder >= offset:
        count += 1

    return count


def lambda_handler(event, context) -> dict:
    get_params = event.get('queryStringParameters')

    if not get_params:
        return {
            'statusCode': 400,
            'body': json.dumps(NEED_DATE_MSG),
        }

    date_str = get_params.get('date')
    if not date_str:
        return {
            'statusCode': 400,
            'body': json.dumps(NEED_DATE_MSG),
        }

    try:
        input_date = parse_date(date_str)
    except ValueError:
        return {
            'statusCode': 400,
            'body': json.dumps('Need date format is YYYY-MM-DD'),
        }

    try:
        week_number = get_week_number_by_date(input_date)
    except SmallDateException as e:
        return {
            'statusCode': 400,
            'body': json.dumps(str(e)),
        }

    return {
        'statusCode': 200,
        'body': json.dumps(f"Week number is {week_number}"),
    }
