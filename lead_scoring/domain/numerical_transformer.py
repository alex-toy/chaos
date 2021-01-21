from sklearn.base import BaseEstimator, TransformerMixin
import lead_scoring.config.config as cf
import logging

logging.basicConfig(format=cf.LOGGING_FORMAT, filename=cf.FILE_LOG, level=logging.INFO)
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger('tcpserver')

class NumericalTransformer(BaseEstimator, TransformerMixin):
    
    def __init__( self ) :
        pass
        
    def fit( self, X, y = None ) :
        return self 

    #Custom transform that replace ouliers by the maximum value 
    def transform(self, X , y = None ):
        logger.info('Run tranform : %s', 'remove outlier for numerical feature', extra=d)
        
        new_X = X.copy()

        #remove outliers
        new_X.loc[new_X [cf.NB_VISITES] > 50,[cf.NB_VISITES]] = 50 
        #new_X.loc[new_X [cf.NB_PAGES_VUES_PAR_VISITE] > 20, [cf.NB_PAGES_VUES_PAR_VISITE]] = 20

        return new_X 