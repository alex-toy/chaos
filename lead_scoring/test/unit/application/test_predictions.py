import os
from pathlib import Path
import pandas as pd
import lead_scoring.config.config as cf
import pickle

def test_predictions() :

    unique_lead_clean = {
    "QUALITE_LEAD": "pourrait etre pertinent",
    "TAGS": "ne pas suivre de formation",
    "DERNIERE_ACTIVITE": "email ouvert",
    "DUREE_SUR_SITEWEB": 0,
    "NB_VISITES": 0
    }
    df = pd.DataFrame(data=unique_lead_clean, index=[0])

    model_file_path = os.path.join(os.path.os.getcwd(), 'models/model_lead_scoring.pkl')

    with open(model_file_path, 'rb') as pickle_file:
        model = pickle.load(pickle_file)

    predict_prob = model.predict_proba(df)[0,1]

    assert predict_prob <= 1
    assert predict_prob >= 0

