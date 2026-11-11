
import unittest
import pandas as pd
import subprocess
import sys

from main import validate_data


class TestSalesData(unittest.TestCase):

    def setUp(self):

        self.df = pd.DataFrame({
            "Month": ["Jan", "Feb"],
            "Product": ["Laptop", "Mobile"],
            "City": ["Lahore", "Kasur"],
            "Revenue": [50000, 30000],
            "Orders": [10, 15],
            "Marketing": [5000, 3000],
            "Discount": [5, 10]
        })

    # Allow Different Data Types During Testing
        self.df = self.df.astype({
            "Revenue": "object",
            "Orders": "object"
        })

# Test 1: Valid Dataset
    def test_valid_data(self):

        results = validate_data(self.df)

        self.assertTrue(all(results.values()))


# Test 2: Empty Dataset
    def test_empty_data(self):

        df = self.df.iloc[0:0]

        results = validate_data(df)
        self.assertFalse(results["Dataset Not Empty"])


# Test 3: Missing Values
    def test_missing_values(self):

        self.df.loc[0, "Revenue"] = None

        results = validate_data(self.df)
        self.assertFalse(results["No Missing Values"])


# Test 4: Duplicate Records
    def test_duplicate_records(self):

        self.df = pd.concat([self.df, self.df.iloc[[0]]], ignore_index=True)

        results = validate_data(self.df)
        self.assertFalse(results["No Duplicate Records"])


# Test 5: Invalid Month
    def test_invalid_month(self):

        self.df.loc[0, "Month"] = "ABC"

        results = validate_data(self.df)
        self.assertFalse(results["Valid Month Values"])


# Test 6: Empty Product Name
    def test_empty_product(self):

        self.df.loc[0, "Product"] = ""

        results = validate_data(self.df)
        self.assertFalse(results["Valid Product Names"])


# Test 7: Empty City Name
    def test_empty_city(self):

        self.df.loc[0, "City"] = ""

        results = validate_data(self.df)
        self.assertFalse(results["Valid City Names"])


# Test 8: Invalid Numeric Value
    def test_invalid_numeric_value(self):

        self.df.loc[0, "Revenue"] = "Invalid"

        results = validate_data(self.df)
        self.assertFalse(results["Valid Numeric Values"])


# Test 9: Negative Revenue
    def test_negative_revenue(self):

        self.df.loc[0, "Revenue"] = -5000

        results = validate_data(self.df)
        self.assertFalse(results["Non-Negative Revenue"])


# Test 10: Negative Orders
    def test_negative_orders(self):

        self.df.loc[0, "Orders"] = -5

        results = validate_data(self.df)
        self.assertFalse(results["Non-Negative Orders"])

# Test 11: Decimal Orders

    def test_decimal_orders(self):

        self.df.loc[0, "Orders"] = 5.5

        results = validate_data(self.df)
        self.assertFalse(results["Whole Number Orders"])

# Test 12: Negative Marketing

    def test_negative_marketing(self):

        self.df.loc[0, "Marketing"] = -1000

        results = validate_data(self.df)
        self.assertFalse(results["Non-Negative Marketing"])

# Test 13: Invalid Discount

    def test_invalid_discount(self):

        self.df.loc[0, "Discount"] = 110

        results = validate_data(self.df)
        self.assertFalse(results["Discount Between 0 and 100"])

# Test 14: Missing Required Column

    def test_missing_column(self):

        df = self.df.drop(columns=["Revenue"])

        results = validate_data(df)
        self.assertFalse(results["Required Columns"])

# Test 15: Import Does Not Run Main Program

    def test_import_does_not_run_program(self):

        result = subprocess.run(
            [sys.executable, "-c", "import main"],
            capture_output=True,
            text=True
        )

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
