import lead_scoring_marieme_alessio.config.config as cf
import os

from sklearn.model_selection import train_test_split

from lead_scoring_marieme_alessio.domain.log_reg_pipeline import log_reg_pipeline
from lead_scoring_marieme_alessio.domain.rand_for_pipeline import rand_for_pipeline
from lead_scoring_marieme_alessio.domain.gb_pipeline import gb_pipeline
from lead_scoring_marieme_alessio.domain.svc_pipeline import svc_pipeline

from lead_scoring_marieme_alessio.domain.evaluate_model import evaluate_model

from lead_scoring_marieme_alessio.infrastructure.clean_data_transformer import CleanDataTransformer

import logging


def train_model() :
    """
    Trains and evaluates models thanks to provided pipelines
    Gives the user information to be able to choose among the models    
    """


    logging.basicConfig(format=cf.LOGGING_FORMAT, filename=cf.FILE_LOG, level=logging.INFO)
    d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
    logger = logging.getLogger('tcpserver')


    logger.info('Run play_file: %s', 'loading data', extra=d)
    cp = CleanDataTransformer(path=cf.FILE_DATA)
    data = cp.load_cleaned_data()
    X = data.drop(cf.TARGET, axis = 1)
    y = data[cf.TARGET]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    nb_expl = str(len(y_test))
    nb_pos_expl = str(sum(y_test))
    nb_neg_expl = str(len(y_test) - sum(y_test))
    print('Number of examples : ' + nb_expl)
    print('Number of positive examples : ' + nb_pos_expl)
    print('Number of negative examples : ' + nb_neg_expl)


    file_path = os.path.join(os.path.os.getcwd(), cf.PERF_FILE)
    f = open(file_path, "a")
    f.truncate(0)
    f.close()

    models = [
        {
            "name" : "Logistic regression", 
            "pipeline" : log_reg_pipeline, 
            "file" : cf.LOG_REG_MODEL_FILE
        },{
            "name" : "Random forest", 
            "pipeline" : rand_for_pipeline, 
            "file" : cf.RF_MODEL_FILE 
        },{
            "name" : "svm", 
            "pipeline" : svc_pipeline, 
            "file" : cf.SVC_MODEL_FILE 
        },{
            "name" : "Gradient boosting", 
            "pipeline" : gb_pipeline, 
            "file" : cf.GB_MODEL_FILE 
        }
    ]


    for model in models : 
        print('*'*50)
        print(model["name"])
        logger.info('Run train_model: %s', f'initiated {model["name"]} training job', extra=d)
        evaluate_model(model["pipeline"], X_train, X_test, y_train, y_test, model["file"])

