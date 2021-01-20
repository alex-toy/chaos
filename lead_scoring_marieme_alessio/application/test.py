from lead_scoring_marieme_alessio.infrastructure.clean_data_transformer import CleanDataTransformer
import pandas as pd
import os
import pickle
from flask import Flask, jsonify, request
import lead_scoring_marieme_alessio.config.config as cf


"""model_file_path = os.path.join(os.path.os.getcwd(), 'chaos/domain/model_lead_scoring.pkl')
with open(model_file_path, 'rb') as pickle_file:
        model = pickle.load(pickle_file)




cd = CleanDataTransformer('/home/mgueye/yotta/chaos-4/data/data.csv')
dataset = cd.load_cleaned_data()
print(dataset.head())

print(dataset.iloc[[0]])

prediction = model.predict_proba(dataset.iloc[0])

print(prediction)"""


def __remove_accents__(df) :
        new_df = df.copy()
        for col in cf.CAT_FEAT :
            new_df[col] = new_df[col].str.lower(
            ).str.replace('[éèê]', 'e', regex=True
            ).str.replace('[ô]', 'o', regex=True
            ).str.replace('[û]', 'u', regex=True
            ).str.replace('[à]', 'a', regex=True)
        return new_df


def pred():
    keys = ["QUALITE_LEAD", "TAGS", "DERNIERE_ACTIVITE", "DUREE_SUR_SITEWEB", "NB_VISITES"]

    answer= {
    "DERNIERE_ACTIVITE": "Conversation Chat",
    "DUREE_SUR_SITEWEB": 13,
    "NB_VISITES": 3,
    "QUALITE_LEAD": "Pas du tout pertinent",
    "TAGS": "Reviendra après avoir lu le courriel",
    "prediction": 1
        }
    df = pd.DataFrame(data=answer, index=[0])
    print(df)
    df = __remove_accents__(df)
    print(df)

    model_file_path = os.path.join(os.path.os.getcwd(), 'chaos/domain/model_lead_scoring.pkl')

    with open(model_file_path, 'rb') as pickle_file:
        model = pickle.load(pickle_file)

    prediction = model.predict_proba(df)
    print(prediction)

    #answer['prediction'] = 1


if __name__ == "__main__":
        pred()
