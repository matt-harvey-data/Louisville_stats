import unittest
import pandas as pd

class LouStatsTest(unittest.TestCase):
    def test_officer_number_columns(self):
        # Define expected columns for validation
        expected_cols = ['badge', 'First_Name', 'Last_Name']
        
        # Create a test DataFrame with the correct columns
        df_correct = pd.DataFrame(columns=expected_cols)
        # Test that columns match exactly
        self.assertEqual(list(df_correct.columns), expected_cols)

        # Create a test DataFrame with missing columns
        df_missing = pd.DataFrame(columns=['badge', 'First_Name'])
        # Test for columns mismatch
        self.assertNotEqual(list(df_missing.columns), expected_cols)

        # Create a test DataFrame with extra columns
        df_extra = pd.DataFrame(columns=['badge', 'First_Name', 'Last_Name', 'Department'])
        # Test for columns mismatch
        self.assertNotEqual(list(df_extra.columns), expected_cols)

# Run the tests
if __name__ == '__main__':
    unittest.main()
