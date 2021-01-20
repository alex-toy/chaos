# PURPOSE: dump the (stupid) model predicting the appetence score of a customer as a pickle file. If run, the model will train and will be saves in chaos/domain/model.pkl
# EXPLANATION: this file should not be used. It's just the source code of the pickle model for your information

import os
import pickle

import numpy as np

from lead_scoring_marieme_alessio.domain.rand_for_pipeline import rand_for_pipeline
from lead_scoring_marieme_alessio.infrastructure.clean_data_transformer import CleanDataTransformer
import lead_scoring_marieme_alessio.config.config as cf
from sklearn.model_selection import train_test_split



def dump_model(model, filename: str):
    with open(filename, 'wb') as handle:
        pickle.dump(model, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    cp = CleanDataTransformer(path=cf.FILE_DATA)
    data = cp.load_cleaned_data()
    X = data.drop(cf.TARGET, axis = 1)
    y = data[cf.TARGET]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    model = rand_for_pipeline(X_train,y_train)
    #DESTINATION_FOLDER = os.path.join("lead_scoring_marieme_alessio".__path__[0], "domain")
    FILENAME = os.path.join(cf.OUTPUTS_MODELS_DIR, "model_lead_scoring.pkl")
    dump_model(model, FILENAME)