# -*- coding: UTF-8 -*-
import numpy as np 
import pandas as pd

import os
import re

import lead_scoring_marieme_alessio.config.config as cf


 
class CleanDataTransformer:
    """
    cleans customer data from raw file
    """
    def __init__(self, path=""):
        self.path = path


    def load_raw_data(self):
        
        _ , extension = os.path.splitext(self.path)
        if extension == '.csv':
            df = pd.read_csv(self.path, sep=';') 
        elif extension == '.parquet':
            df = pd.read_parquet(self.path)
        else:
            raise FileExistsError('Extension must be parquet or csv.')

        return df


    def load_cleaned_data(self):
        
        _ , extension = os.path.splitext(self.path)
        if extension == '.csv':
            df = pd.read_csv(self.path, sep=';') 
        elif extension == '.parquet':
            df = pd.read_parquet(self.path)
        else:
            raise FileExistsError('Extension must be parquet or csv.')

        return self._clean_data(df)



    def _clean_data(self, df): 
        df = self.__change_columns_names__(df)
        df = self.__select_columns__(df, cf.COLS_TO_KEEP)
        df = self.__remove_accents__(df)
        return df

    

    def __change_columns_names__(self, df):
        new_df = df.copy()
        new_df = new_df[cf.COL_NAME_TRAIN]
        new_df.columns = cf.NEW_COL_NAMES
        return new_df


    def __select_columns__(self, data, cols_to_keep) :
        new_df = data.copy()
        return new_df[cols_to_keep]



    def __remove_accents__(self, df) :
        new_df = df.copy()
        for col in cf.CAT_FEAT :
            new_df[col] = new_df[col].str.lower(
            ).str.replace('[éèê]', 'e', regex=True
            ).str.replace('[ô]', 'o', regex=True
            ).str.replace('[û]', 'u', regex=True
            ).str.replace('[à]', 'a', regex=True)
        return new_df













