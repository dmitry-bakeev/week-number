#!/usr/bin/env python3
import unittest

from datetime import date

from main import get_week_number_by_date, SmallDateException


class GetWeekNumberByDate(unittest.TestCase):

    def test_exception(self) -> None:
        with self.assertRaises(SmallDateException) as context:
            get_week_number_by_date(date(2018, 1, 1))

    def test_normalfirst_week(self) -> None:
        input_values = (
            date(2019, 1, 1),
            date(2019, 1, 2),
            date(2019, 1, 3),
            date(2019, 1, 4),
            date(2019, 1, 5),
        )
        output_value = 1
        results = (get_week_number_by_date(item) for item in input_values)
        for value in results:
            self.assertEqual(value, output_value)

    def test_normal_second_week(self) -> None:
        input_values = (
            date(2019, 1, 6),
            date(2019, 1, 7),
            date(2019, 1, 8),
            date(2019, 1, 9),
            date(2019, 1, 10),
            date(2019, 1, 11),
            date(2019, 1, 12),
        )
        output_value = 2
        results = (get_week_number_by_date(item) for item in input_values)
        for value in results:
            self.assertEqual(value, output_value)

    def test_normal_tenth_week(self) -> None:
        input_values = (
            date(2019, 3, 3),
            date(2019, 3, 4),
            date(2019, 3, 5),
            date(2019, 3, 6),
            date(2019, 3, 7),
            date(2019, 3, 8),
            date(2019, 3, 9),
        )
        output_value = 10
        results = (get_week_number_by_date(item) for item in input_values)
        for value in results:
            self.assertEqual(value, output_value)

    def test_normal_eleventh_week(self) -> None:
        input_values = (
            date(2019, 3, 10),
            date(2019, 3, 11),
            date(2019, 3, 12),
            date(2019, 3, 13),
            date(2019, 3, 14),
            date(2019, 3, 15),
            date(2019, 3, 16),
        )
        output_value = 11
        results = (get_week_number_by_date(item) for item in input_values)
        for value in results:
            self.assertEqual(value, output_value)


if __name__ == '__main__':
    unittest.main()
