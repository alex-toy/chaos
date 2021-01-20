# -*- coding: UTF-8 -*-
import lead_scoring_marieme_alessio.config.config as cf
import os
from os import listdir
from os.path import isfile, join

import numpy as np 
import pandas as pd

from sklearn.model_selection import train_test_split

from lead_scoring_marieme_alessio.infrastructure.clean_data_transformer import CleanDataTransformer
from lead_scoring_marieme_alessio.domain.log_reg_pipeline import log_reg_pipeline
from lead_scoring_marieme_alessio.domain.rand_for_pipeline import rand_for_pipeline
from lead_scoring_marieme_alessio.domain.gb_pipeline import gb_pipeline

import logging

from joblib import dump, load




def model_prediction(file_path, model_file, save_file) :
    """
    Produces a csv files from raw_data thanks to provided model
    csv file is to be found in output directory and has two new columns
    One predictions column and one probability column
    """
    model = load(os.path.join(cf.OUTPUTS_MODELS_DIR, model_file)) 

    def probability_predictions(model, data, raw_data) :
        new_X = raw_data.copy()
        new_X[cf.PRED_PROBA_COL_NAME] = model.predict_proba(data)[:,1]
        new_X[cf.PRED_COL_NAME] = model.predict(data)
        return new_X

    cd = CleanDataTransformer(path=file_path)
    data = cd.load_cleaned_data()
    raw_data = cd.load_raw_data()

    preds = probability_predictions(model, data, raw_data)
    preds.to_csv(os.path.join(cf.OUTPUTS_DIR, save_file))



def get_output_files() : 
    model_files = [f for f in listdir(cf.OUTPUTS_MODELS_DIR) if isfile(join(cf.OUTPUTS_MODELS_DIR, f)) and not f.startswith('.')]
    i = 1
    model_dict = dict()
    output_files = dict()
    for model_file in model_files :
        model_dict[i] = model_file
        output_files[i] = model_file[:-7] + cf._SAVED_FILENAME
        print(str(i) + ' : ' + model_file)
        i += 1
    return output_files, model_dict




def choose_model() :
    """
    Gives the user the opportunity to choose among all available models.
    """
    print('\nChoose your model :')
    
    output_files, model_dict = get_output_files()

    model_choice = input('Number of chosen model (defaults to 1) : ')
    if model_choice == '' : model_choice = 1
    print('model_choice : ' + str(model_choice))
    chosen_model = model_dict[int(model_choice)]
    chosen_output_file = output_files[int(model_choice)]

    print('You have chosen model : ' + chosen_model)

    return chosen_model, chosen_output_file


def best_model() :
    """
    Automatically selects best model based on precision.
    """
    file_path = os.path.join(os.path.os.getcwd(), cf.PERF_FILE)
    with open(file_path, 'r') as perf_file:
        prec = perf_file.readlines()[0].split(';')

    precisions = [t for t in prec if len(t)>0]

    models = [t.split(':')[0] for t in precisions]
    models = sorted(models)
    precisions = np.array([float(t.split(':')[1]) for t in precisions])
    index_best_model = np.argmax(precisions)
    #best_model = models[index_best_model]

    output_files, model_dict = get_output_files()

    chosen_model = model_dict[int(index_best_model)+1]
    chosen_output_file = output_files[int(index_best_model)+1]

    print('Best model is ' + chosen_model + ' with precision ' + str(max(precisions)) + '%')

    return chosen_model, chosen_output_file

   



def prediction_workflow() :
    """
    Acompanies final user in his quest for predictions
    User needs to put his raw csv file on which he wants to get predictions at the root of the project ; 
    Default name for the csv file is data.csv
    User can choose among all the available .joblib in models directory
    Prediction file is provided in output directory
    """

    logging.basicConfig(format=cf.LOGGING_FORMAT, filename=cf.FILE_LOG, level=logging.INFO)
    d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
    logger = logging.getLogger('tcpserver')

    print('Put your file in the predict folder.')
    name_file = input('Name of the file to get predictions for (defaults to predict/data.csv) : ')
    if name_file == '' : name_file = 'data.csv'
    
    temp = os.path.join('predict', name_file)
    file_path = os.path.join(os.path.os.getcwd(), temp)
    print(file_path)
    cd =  CleanDataTransformer(path=file_path)

    print('Choose strategy :')
    print('1 : choose among all models')
    print('2 : let app choose best model for you (based on precision)')
    strategy_choice = input('Your strategy choice (defaults to 1) : ')
    if strategy_choice == '' : strategy_choice = '1'

    if strategy_choice == '1' :
        chosen_model, chosen_output_file = choose_model()
    if strategy_choice == '2' :
        chosen_model, chosen_output_file = best_model()


    model_prediction(file_path, chosen_model, chosen_output_file)
    pred_file_path = os.path.join(cf.OUTPUTS_DIR, chosen_output_file)
    print('You can now get your prediction file at : ' + pred_file_path)
    return chosen_output_file




def get_leads(saved_file, threshold) :
    """
    Allows user to place a threshold on the rows he wants to retrieve
    """

    pred_file_path = os.path.join(cf.OUTPUTS_DIR, saved_file)
    data = pd.read_csv(pred_file_path)
    return data[data[cf.PRED_PROBA_COL_NAME] > threshold]



