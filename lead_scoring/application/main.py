# -*- coding: UTF-8 -*-
import lead_scoring_marieme_alessio.config.config as cf
import os
from os import listdir
from os.path import isfile, join

import numpy as np 
import pandas as pd


from lead_scoring_marieme_alessio.application.train_model import train_model
from lead_scoring_marieme_alessio.application.predict import prediction_workflow, get_leads


if __name__ == '__main__':

    print('Choose action :')
    print('1 : train new model')
    print('2 : make prediction')
    choice = input('Your choice (defaults to 1) : ')
    if choice == '' : choice = '1'

    if choice == '1' :
        train_model()
    if choice == '2' :
        file_name = prediction_workflow()
        threshold = input('insert threshold : ')
        data = get_leads(file_name, float(threshold))
        print(data[['ID_CLIENT', 'PREDICTED_PROBABILITY', 'PREDICTION']])

    