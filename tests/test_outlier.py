# test_outlier.py
import os
import sys
import unittest
import pandas as pd
import numpy as np

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.outlier import Outlier  # Replace 'your_module' with the actual name of your module

class TestOutlier(unittest.TestCase):
    def setUp(self):
        # Optional: Set up any resources or perform any setup actions before each test method runs
        pass

    def tearDown(self):
        # Optional: Clean up any resources or perform any cleanup actions after each test method runs
        pass

    def test_handle_outliers(self):
        # Test handle_outliers method

        # Create a sample DataFrame for testing
        data = {'col1': [1, 2, 3, 1000],
                'col2': [4, 5, 6, 10000]}
        df = pd.DataFrame(data)

        outlier_obj = Outlier(df)
        cols_to_process = ['col1', 'col2']

        # Apply the handle_outliers method
        result_df = outlier_obj.handle_outliers(df.copy(), cols_to_process)

        # Assert that the result is a DataFrame
        self.assertIsInstance(result_df, pd.DataFrame)

        # Additional assertions based on your expectations
        # ...

    def test_calculate_num_outliers_zscore(self):
        # Test calculate_num_outliers_zscore method

        # Create a sample DataFrame for testing
        data = {'col1': [1, 2, 3, 1000]}
        df = pd.DataFrame(data)

        outlier_obj = Outlier(df)

        # Apply the calculate_num_outliers_zscore method
        result_outliers = outlier_obj.calculate_num_outliers_zscore(df['col1'])

        # Assert that the result is a list
        self.assertIsInstance(result_outliers, list)

        # Additional assertions based on your expectations
        # ...

    def test_calculate_num_outliers_iqr(self):
        # Test calculate_num_outliers_iqr method

        # Create a sample DataFrame for testing
        data = {'col1': [1, 2, 3, 1000]}
        df = pd.DataFrame(data)

        outlier_obj = Outlier(df)
        cols_to_process = ['col1']

        # Apply the calculate_num_outliers_iqr method
        result_outliers = outlier_obj.calculate_num_outliers_iqr(df, cols_to_process)

        # Assert that the result is a dictionary
        self.assertIsInstance(result_outliers, dict)

        # Additional assertions based on your expectations
        # ...

    def test_outlier_overview(self):
        # Test outlier_overview method

        # Create a sample DataFrame for testing
        data = {'col1': [1, 2, 3, 1000],
                'total_ul_(bytes)': [100, 200, 300, 10000]}
        df = pd.DataFrame(data)

        outlier_obj = Outlier(df)
        col_to_check = 'col1'

        # Apply the outlier_overview method
        result_df = outlier_obj.outlier_overview(df, col_to_check)

        # Assert that the result is a DataFrame
        self.assertIsInstance(result_df, pd.DataFrame)

        # Additional assertions based on your expectations
        # ...

if __name__ == '__main__':
    unittest.main()
