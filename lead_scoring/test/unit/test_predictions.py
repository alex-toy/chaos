import os
import chaos
from lead_scoring.test.unit.payload import unique_lead, multiple_lead
from pathlib import Path
from flask import Flask, jsonify, request
import pandas as pd

import lead_scoring.config.config as cf
from lead_scoring.infrastructure.clean_data_transformer import CleanDataTransformer

import  pickle
import os
import pandas as pd
import csv


def test_model_file_exists():
    model = os.path.join(lead_scoring.__path__[0], "models/model_lead_scoring.pkl")
    assert os.path.isfile(model)




def test_model_predicts_correctly() :
    keys = cf.NEW_COL_NAMES_PRED[1:]

    df = pd.DataFrame(data=unique_lead, index=[0])
    cdt = CleanDataTransformer(is_train=False, df=df)
    df = cdt.load_cleaned_data()

    model_file_path = os.path.join(lead_scoring.__path__[0], "models/model_lead_scoring.pkl")

    with open(model_file_path, 'rb') as pickle_file:
        model = pickle.load(pickle_file)

    predict_prob = model.predict_proba(df)[0,1]
    predict = model.predict(df)[0]

    assert predict_prob <= 1
    assert predict_prob >= 0

