import numpy as np 
import pandas as pd

import json 

import os
import os.path
from os import path

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler, LabelEncoder, LabelBinarizer, OrdinalEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import FeatureUnion, Pipeline, make_pipeline
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, KFold
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn import svm, datasets


import lead_scoring_marieme_alessio.config.config as cf
from lead_scoring_marieme_alessio.infrastructure.clean_data_transformer import CleanDataTransformer
from lead_scoring_marieme_alessio.domain.categorical_transformer import CategoricalTransformer
from lead_scoring_marieme_alessio.domain.numerical_transformer import NumericalTransformer
from lead_scoring_marieme_alessio.domain.feature_selector import FeatureSelector
from lead_scoring_marieme_alessio.domain.pipeline_transformer import pipeline_transformer



def rand_for_pipeline(X_train, y_train):
    
    full_pipeline = pipeline_transformer()

    param_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../notebook/best_params.json'))

    criterion = 'gini'
    max_depth = None
    min_samples_leaf = 1
    min_samples_split = 2
    n_estimators = 100
    
    if path.isfile(param_path) :
        with open(param_path) as param_file:
            data = json.load(param_file)
            if 'random_forest' in data.keys():
                params = data['random_forest']
                if 'criterion' in params.keys():
                    criterion = params['criterion']
                if 'max_depth' in params.keys():
                    max_depth = params['max_depth']
                if 'min_samples_leaf' in params.keys():
                    min_samples_leaf = params['min_samples_leaf']
                if 'min_samples_split' in params.keys():
                    min_samples_split = params['min_samples_split']
                if 'n_estimators' in params.keys():
                    n_estimators = params['n_estimators']  

    rf_pipeline = Pipeline( steps = [ 
        ( 'full_pipeline', full_pipeline),
        ( 'rf', RandomForestClassifier(
                    criterion=criterion,
                    max_depth=max_depth,
                    min_samples_leaf=min_samples_leaf,
                    min_samples_split=min_samples_split,
                    n_estimators=n_estimators
                )) 
    ])


    rf_pipeline.fit( X_train, y_train )


    return rf_pipeline


























