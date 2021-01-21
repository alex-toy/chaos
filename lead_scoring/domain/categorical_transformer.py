import numpy as np 
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
import lead_scoring.config.config as cf
import logging

logging.basicConfig(format=cf.LOGGING_FORMAT, filename=cf.FILE_LOG, level=logging.INFO)
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger('tcpserver')



class CategoricalTransformer( BaseEstimator, TransformerMixin ):
    
    def __init__(self) :
        pass
        

        
    def fit( self, X, y = None  ):
        return self



    def __handle_column__(self, obj, feature_values):
        if not isinstance(obj, str) : return 'other'
        if obj in feature_values : return obj
        return 'other'
    
    
    
    def transform(self, X , y = None ):

        logger.info('Run tranform : %s', 'initiated column processing', extra=d)

        new_X = X.copy()

        for col, use_list in zip(cf.CAT_FEAT, cf.use_lists):
            new_X[col] = new_X[col].apply( lambda row : self.__handle_column__(row, use_list) )

        return new_X
    






















