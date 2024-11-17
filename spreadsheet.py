class SpreadSheet:
    def __init__(self):
        # Initialize an empty spreadsheet
        self.data = []

    def add_row(self, row):
        """Add a row to the spreadsheet"""
        self.data.append(row)

    def get_row(self, index):
        """Retrieve a row at a specific index"""
        if 0 <= index < len(self.data):
            return self.data[index]
        raise IndexError("Index out of range")

    def clear(self):
        """Clear all rows from the spreadsheet"""
        self.data.clear()
