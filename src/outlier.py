import sys

import numpy as np
import pandas as pd


class Outlier:
    def __init__(self, df: pd.DataFrame):
        """Initialize the PreProcess class.

        Args:
            df (pd.DataFrame): dataframe to be preprocessed
        """
        try:
            self.df = df
        except Exception:
            sys.exit(1)

    # how many missing values exist or better still what is the % of missing values in the dataset?

    def handle_outliers(self, df: pd.DataFrame, cols):
        """Handle outliers in the dataset.

        Args:
            df (pd.DataFrame): a dataframe to be preprocessed

        Returns:
            pd.DataFrame: the dataframe
        """
        # Get numerical columns
        # num_cols = df.select_dtypes(include=np.number).columns
        for col in cols:
            # Computing 10th, 90th percentiles and replacing the outliers
            df[col] = [np.log(x) for x in df[col]]
        return df

    def calculate_num_outliers_zscore(self, col):
        """Return the number of outliers for each numerical col.

        Args:
            col (pd.DataFrame): a dataframe to be analyzed
        """
        # calculate skewness
        outliers = []

        thres = 3
        mean = np.mean(col)
        std = np.std(col)
        # print(mean, std)
        for i in col:
            z_score = (i-mean)/std
            if (np.abs(z_score) > thres):
                outliers.append(i)
        return outliers  # Driver code

        # sample_outliers = detect_outliers_zscore(
        #     df['nb_of_sec_with_vol_ul_<_1250b'])
        # print("Outliers from Z-scores method: ", len(sample_outliers))

    def calculate_num_outliers_iqr(self, df, cols):
        """Return the number of outliers for each col.

        Args:
            df (pd.DataFrame): a dataframe to be analyzed
            cols (list): list of columns to analyze
        """
        outliersTot = {}

        for col in cols:
            outliers = []
            df_sorted = df.sort_values(col)[col]
            q1 = np.percentile(df_sorted, 25)
            q3 = np.percentile(df_sorted, 75)

            IQR = q3 - q1
            lwr_bound = q1 - (1.5 * IQR)
            upr_bound = q3 + (1.5 * IQR)

            for i in df_sorted:
                if (i < lwr_bound or i > upr_bound):
                    outliers.append(i)

            outliersTot[col] = outliers

        return outliersTot


    def outlier_overview(self, df, col):
        """Get outlier overview.

        Args:
            df (pd.DataFrame): a dataframe to be analyzed
        """

        # calculate upper and lower limits
        upper_limit = df[col].mean() + 3 * df['total_ul_(bytes)'].std()
        lower_limit = df[col].mean() - 3 * df['total_ul_(bytes)'].std()

        # select outliers
        return df[~((df[col] < upper_limit) & (df[col] > lower_limit))]

        # # outliers removed
        # display(df[(df[col] < upper_limit) & (df[col] > lower_limit)])
