

import unittest
from datetime import datetime


class TestProject3Inputs(unittest.TestCase):

    def test_symbol(self):
        symbol = "AAPL"
        self.assertTrue(symbol.isalpha())
        self.assertTrue(symbol.isupper())
        self.assertTrue(1 <= len(symbol) <= 7)

    def test_chart_type(self):
        chart_type = "1"
        self.assertIn(chart_type, ["1", "2"])

    def test_time_series(self):
        time_series = "4"
        self.assertIn(time_series, ["1", "2", "3", "4"])

    def test_start_date(self):
        start_date = "2024-01-01"
        self.assertIsNotNone(
            datetime.strptime(start_date, "%Y-%m-%d")
        )

    def test_end_date(self):
        end_date = "2024-12-31"
        self.assertIsNotNone(
            datetime.strptime(end_date, "%Y-%m-%d")
        )


if __name__ == "__main__":
    unittest.main()