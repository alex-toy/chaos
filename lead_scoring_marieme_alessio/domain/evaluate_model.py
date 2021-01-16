import numpy as np 
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler, LabelEncoder, LabelBinarizer, OrdinalEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import FeatureUnion, Pipeline, make_pipeline
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, KFold
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn import svm, datasets

import matplotlib.pyplot as plt
import seaborn as sns

import lead_scoring_marieme_alessio.config.config as cf
from lead_scoring_marieme_alessio.infrastructure.clean_data_transformer import CleanDataTransformer
from lead_scoring_marieme_alessio.domain.categorical_transformer import CategoricalTransformer
from lead_scoring_marieme_alessio.domain.numerical_transformer import NumericalTransformer
from lead_scoring_marieme_alessio.domain.feature_selector import FeatureSelector
from joblib import dump, load
import os


def display_model_performance(y_test, y_pred, model_name) :
    #accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    file_path = os.path.join(os.path.os.getcwd(), cf.PERF_FILE)

    acc = str(round(accuracy_score(y_test, y_pred)*100, 2))
    prec = str(round(cm[1][1]/sum(y_test)*100, 2))

    with open(file_path, 'a') as perf_file:
        perf_file.write(model_name + ':' + prec + ';')

    print(cm)
    print('Accuracy : ' + acc + '%')
    print('Precision : ' + prec + '%')




def evaluate_model(model, X_train, X_test, y_train, y_test, model_name='model.joblib') :

    model = model(X_train, y_train)
    dump(model, os.path.join(cf.OUTPUTS_MODELS_DIR, model_name)) 
    y_pred = model.predict( X_test )

    display_model_performance(y_test, y_pred, model_name) 
    
