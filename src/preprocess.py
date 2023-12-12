import re

class PreProcess:
    def __init__(self):
        pass

    def remove_duplicate(self, data):
        return data.drop_duplicates()
    
    def remove_missing(self, data):
        '''
        This function removes all columns 
        with missing values of above 30%
        '''
        return data.dropna(thresh=len(data)*0.7, axis=1)
        