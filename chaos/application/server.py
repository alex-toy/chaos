import datetime
from flask import Flask, jsonify, request

from chaos.infrastructure.config.config import config

import  pickle
import os
import pandas as pd


app = Flask(__name__)
PORT = config["api"]["port"]
HOST = config["api"]["host"]


def model_prediction(data_file_path, model_file_path, save_file) :
    """
    Produces a csv files from raw_data thanks to provided model
    csv file is to be found in output directory and has two new columns
    One predictions column and one probability column
    """
    model = pickle.load(model_file_path) 

    def probability_predictions(model, data, raw_data) :
        new_X = raw_data.copy()
        new_X[cf.PRED_PROBA_COL_NAME] = model.predict_proba(data)[:,1]
        new_X[cf.PRED_COL_NAME] = model.predict(data)
        return new_X

    cd = CleanDataTransformer(path=data_file_path)
    data = cd.load_cleaned_data()
    raw_data = cd.load_raw_data()

    preds = probability_predictions(model, data, raw_data)
    preds.to_csv(os.path.join(cf.OUTPUTS_DIR, save_file))


@app.route("/example", methods=["GET"])
def example():
    try:
        initial_number = request.get_json()["question"]
        answer = float(initial_number)*2
    except (ValueError, TypeError, KeyError):
        DEFAULT_RESPONSE = 0
        answer = DEFAULT_RESPONSE
    response = {"answer": answer}
    return jsonify(response)


@app.route("/prospect", methods=["POST"])
def prospect():

    model_file_path = os.path.join(os.path.os.getcwd(), 'chaos/domain/model.pkl')

    data_file_path=''

    data_file_path = request.files['file']
    #print(data_file)
    #print(pd.read_csv(data_file, sep=';'))

    model_prediction(data_file_path, model_file_path, os.path.os.getcwd())



    try:
        initial_number = request.get_json()["question"]
        answer = float(initial_number)*2
    except (ValueError, TypeError, KeyError):
        DEFAULT_RESPONSE = 0
        answer = DEFAULT_RESPONSE
    response = {"answer": answer}
    return jsonify(response)


if __name__ == "__main__":
    print("starting API at", datetime.datetime.now())
    app.run(debug=False, host=HOST, port=PORT)
