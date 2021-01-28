import datetime
from flask import Flask, jsonify, request
from flask import send_file, send_from_directory, safe_join, abort

from lead_scoring.infrastructure.config.config import config
import lead_scoring.config.config as cf
from lead_scoring.infrastructure.clean_data_transformer import CleanDataTransformer
from lead_scoring.infrastructure.connexion import Connexion
import lead_scoring.infrastructure.database as db
import lead_scoring.infrastructure.retrieve_model as r_model



import  pickle
import os
import pandas as pd
import csv


app = Flask(__name__)
PORT = config["api"]["port"]
HOST = config["api"]["host"]



@app.route("/pred", methods=["GET"])
def pred():
    keys = cf.FEATURES_PRED

    try:
        answer = {key : request.get_json()[key] for key in keys}
    except (ValueError, TypeError, KeyError):
        DEFAULT_RESPONSE = 0
        answer = DEFAULT_RESPONSE
   
    df = pd.DataFrame(data=answer, index=[0])
    id_client = df['ID_CLIENT']
    print("#######################################################")
    print(id_client)
    df = df.drop('ID_CLIENT', axis=1)
    cdt = CleanDataTransformer(is_train=False, df=df)
    df = cdt.load_cleaned_data()
    model = r_model.retrieve_model("chaos-4", "model_lead_scoring.pkl")
    

    predict_prob = int(model.predict_proba(df)[0,1])
    predict = model.predict(df)[0]
    prediction = {}
    prediction[0] = {"id_lead":int(id_client),"prediction":int(predict)}
    return  prediction


@app.route("/preds", methods=["GET"])
def preds():

    model =  r_model.retrieve_model("chaos-4", "model_lead_scoring.pkl")

    ids = list(request.get_json().keys())

    answer = {id_ : {
        **{ "id_client": int(pd.DataFrame(data=request.get_json()[id_],index=[0])["ID_CLIENT"]),
            "prediction" : 
            int(model.predict(
                CleanDataTransformer(is_train=False, df=pd.DataFrame(data=request.get_json()[id_],index=[0]).drop("ID_CLIENT", axis=1))
            .load_cleaned_data())[0])
        }
    } for id_ in ids}

    return  answer




@app.route("/training", methods=["POST"])
def training():

    model_file_path = os.path.join(os.path.os.getcwd(), 'models/model.pkl')
    
    data_file_path = request.files['file']
    print(data_file_path)

    #model_prediction(data_file_path, model_file_path, os.path.os.getcwd())

    data_prediction_file_path = os.path.os.getcwd()
    try:
        return send_from_directory(data_prediction_file_path, filename="data_pred.csv", as_attachment=True)
    except FileNotFoundError:
        abort(404)


@app.route("/get_leads_with_limit", methods=["GET"])
def get_leads_with_limit():
    key = "limit"
    try:
        answer = {key : request.get_json()[key]}
    except (ValueError, TypeError, KeyError):
        DEFAULT_RESPONSE = 0
        answer = DEFAULT_RESPONSE
    if answer == 0:
        prediction = 0
        return prediction
    else:    
        prediction = db.get_leads_with_limit(answer[key])
        return  prediction

@app.route("/get_leads_with_ids", methods=["GET"])
def get_leads_with_ids():
    key = "ids"
    try:
        answer = {key : request.get_json()[key]}
    except (ValueError, TypeError, KeyError):
        DEFAULT_RESPONSE = 0
        answer = DEFAULT_RESPONSE
    if answer == 0:
        prediction = 0
        return prediction
    else:    
        prediction = db.get_leads_with_ids(tuple(answer[key]))
        return  prediction


        

if __name__ == "__main__":
    print("starting API at", datetime.datetime.now())
    app.run(debug=False, host=HOST, port=PORT)
