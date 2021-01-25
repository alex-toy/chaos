from sklearn.base import BaseEstimator, TransformerMixin
import lead_scoring.config.config as cf
import logging


class NumericalTransformer(BaseEstimator, TransformerMixin):
    
    def __init__( self ) :
        pass
        
    def fit( self, X, y = None ) :
        return self 

    #Custom transform that replace ouliers by the maximum value 
    def transform(self, X , y = None ):
        
        new_X = X.copy()

        #remove outliers
        new_X.loc[new_X [cf.NB_VISITES] > 50,[cf.NB_VISITES]] = 50 
        #new_X.loc[new_X [cf.NB_PAGES_VUES_PAR_VISITE] > 20, [cf.NB_PAGES_VUES_PAR_VISITE]] = 20

        return new_X 