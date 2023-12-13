import numpy as np
import pandas as pd
from scipy import stats

class PreProcess:
    def __init__(self, data):
        self.data = data

    def remove_duplicate(self):
        return self.data.drop_duplicates()

    def remove_missing(self):
        '''
        This function removes all columns 
        with missing values of above 30%
        '''
        self.data = self.data.dropna(thresh=len(self.data)*0.7, axis=1)
        return self.data

    def convert_to_timestamp(self, column_name):
        '''
        This function converts the date column to timestamp
        '''
        self.data[column_name] = pd.to_datetime(self.data[column_name])
        return self.data
    
    def impute_mean_numeric(self):
        '''
        This function imputes mean values to missing values in numeric columns
        '''
        numeric_columns = self.data.select_dtypes(include=['float64', 'number']).columns
        self.data.loc[:, numeric_columns] = self.data.loc[:, numeric_columns].apply(lambda x: x.fillna(x.mean()))
        return self.data

    
    def impute_mean_datetime(self):
        '''
        This function imputes mean values to missing values in datetime columns
        '''
        datetime_columns = self.data.select_dtypes(include=['datetime64']).columns

        for col in datetime_columns:
            mean_timestamp = self.data[col].mean().timestamp()
            self.data.loc[:, col] = self.data[col].fillna(pd.to_datetime(mean_timestamp, unit='s'))

        return self.data
    
    def impute_mode_categorical(self):
        '''
        This function imputes mode values to missing values in categorical columns
        '''
        categorical_columns = self.data.select_dtypes(include=['object']).columns

        for col in categorical_columns:
            self.data.loc[:, col] = self.data[col].fillna(self.data[col].mode()[0])

        return self.data

    def remove_outliers(self):
        '''
        This function removes outliers from the dataset for numeric fields
        '''
        numeric_columns = self.data.select_dtypes(include=['float64', 'number']).columns
        z_scores = np.abs(stats.zscore(self.data[numeric_columns]))
        filtered_data = self.data[(z_scores < 3).all(axis=1)]
        return filtered_data
