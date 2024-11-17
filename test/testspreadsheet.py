import unittest
from spreadsheet import SpreadSheet

class TestSpreadSheet(unittest.TestCase):
    def setUp(self):
        """Setup a new spreadsheet instance before each test"""
        self.spreadsheet = SpreadSheet()

    def test_add_row(self):
        """Test adding a row to the spreadsheet"""
        self.spreadsheet.add_row([1, 2, 3])
        self.assertEqual(self.spreadsheet.data, [[1, 2, 3]])

    def test_get_row_valid(self):
        """Test retrieving a valid row from the spreadsheet"""
        self.spreadsheet.add_row([1, 2, 3])
        self.spreadsheet.add_row([4, 5, 6])
        self.assertEqual(self.spreadsheet.get_row(1), [4, 5, 6])

    def test_get_row_invalid(self):
        """Test retrieving a row with an invalid index"""
        with self.assertRaises(IndexError):
            self.spreadsheet.get_row(10)

    def test_clear(self):
        """Test clearing all rows from the spreadsheet"""
        self.spreadsheet.add_row([1, 2, 3])
        self.spreadsheet.clear()
        self.assertEqual(self.spreadsheet.data, [])

if __name__ == "__main__":
    unittest.main()
