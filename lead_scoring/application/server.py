import datetime
from flask import Flask, jsonify, request
from flask import send_file, send_from_directory, safe_join, abort

from lead_scoring.infrastructure.config.config import config
import lead_scoring.config.config as cf
from lead_scoring.infrastructure.clean_data_transformer import CleanDataTransformer

import  pickle
import os
import pandas as pd
import csv


app = Flask(__name__)
PORT = config["api"]["port"]
HOST = config["api"]["host"]



@app.route("/pred", methods=["POST"])
def pred():
    keys = cf.FEATURES

    try:
        answer = {key : request.get_json()[key] for key in keys}
    except (ValueError, TypeError, KeyError):
        DEFAULT_RESPONSE = 0
        answer = DEFAULT_RESPONSE

    df = pd.DataFrame(data=answer, index=[0])
    cdt = CleanDataTransformer(is_train=False, df=df)
    df = cdt.load_cleaned_data()

    model_file_path = os.path.join(os.path.os.getcwd(), 'models/model_lead_scoring.pkl')

    with open(model_file_path, 'rb') as pickle_file:
        model = pickle.load(pickle_file)

    
    predict_prob = model.predict_proba(df)[0,1]
    predict= model.predict(df)[0]
    #response = {"prediction":predict} #, "predict_proba":predict_prob} 
    answer['prediction'] = int(predict)
    answer['predict_proba'] = float(predict_prob)
    return  answer #{"prediction":int(predict)} #jsonify(response)


@app.route("/preds", methods=["POST"])
def preds():

    model_file_path = os.path.join(os.path.os.getcwd(), 'models/model_lead_scoring.pkl')

    with open(model_file_path, 'rb') as pickle_file:
        model = pickle.load(pickle_file)

    ids = list(request.get_json().keys())
    keys = cf.NEW_COL_NAMES_PRED[1:]

    answer = {id_ : {
        **request.get_json()[id_],
        **{"predict_proba" : 
            model.predict_proba(
                CleanDataTransformer(is_train=False, df=pd.DataFrame(data=request.get_json()[id_], index=[0])
            ).load_cleaned_data())[0,1]
        }
    } for id_ in ids}

    return  answer



@app.route("/training", methods=["POST"])
def training():

    model_file_path = os.path.join(os.path.os.getcwd(), 'models/model.pkl')
    
    data_file_path = request.files['file']
    print(data_file_path)

    model_prediction(data_file_path, model_file_path, os.path.os.getcwd())

    data_prediction_file_path = os.path.os.getcwd()
    try:
        return send_from_directory(data_prediction_file_path, filename="data_pred.csv", as_attachment=True)
    except FileNotFoundError:
        abort(404)






if __name__ == "__main__":
    print("starting API at", datetime.datetime.now())
    app.run(debug=False, host=HOST, port=PORT)
