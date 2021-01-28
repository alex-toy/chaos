from lead_scoring.infrastructure.connexion import Connexion
from lead_scoring.infrastructure.clean_data_transformer import CleanDataTransformer
import pandas as pd
import os
import pickle


def get_leads_with_limit(limit:int=10):
    query = """SELECT ID_CLIENT, QUALITE_LEAD,TAGS,DERNIERE_ACTIVITE,DUREE_SUR_SITEWEB, NB_VISITES
            FROM labeled_lead_scoring 
            LIMIT {nb_leads}
            """.format( nb_leads= int(limit))
    
    engine = Connexion().connect()
    df = pd.read_sql(query, engine)

    id_leads= df["id_client"]
    df = df.drop("id_client", axis = 1)

    cdt = CleanDataTransformer(is_train=False, df=df)
    df = cdt.load_cleaned_data()

    model_file_path = os.path.join(os.path.os.getcwd(), 'models/model_lead_scoring.pkl')

    with open(model_file_path, 'rb') as pickle_file:
        model = pickle.load(pickle_file)

    predict= model.predict(df)
    df['LEAD'] = predict

    prediction = {}
    for i, id_lead in enumerate(id_leads):
        prediction["{num}".format( num = int(i))] = {'id_lead':int(id_lead), 'prediction':int(predict[i])}
    return prediction


def get_leads_with_ids (ids: tuple = None):
    if len(ids)==1:
        query = """SELECT ID_CLIENT, QUALITE_LEAD,TAGS,DERNIERE_ACTIVITE,DUREE_SUR_SITEWEB, NB_VISITES
            FROM labeled_lead_scoring 
            WHERE ID_CLIENT = {id_client}
            """.format(id_client= int(ids[0]))
    else:
        query = """SELECT ID_CLIENT, QUALITE_LEAD,TAGS,DERNIERE_ACTIVITE,DUREE_SUR_SITEWEB, NB_VISITES
                FROM labeled_lead_scoring 
                WHERE ID_CLIENT in {id_client}
                """.format(id_client= ids)
    
    engine = Connexion().connect()
    df = pd.read_sql(query, engine)

    id_leads= df["id_client"]
    df = df.drop("id_client", axis = 1)

    cdt = CleanDataTransformer(is_train=False, df=df)
    df = cdt.load_cleaned_data()

    model_file_path = os.path.join(os.path.os.getcwd(), 'models/model_lead_scoring.pkl')

    with open(model_file_path, 'rb') as pickle_file:
        model = pickle.load(pickle_file)

    predict= model.predict(df)
    df['LEAD'] = predict

    prediction = {}

    if  len(ids)==1:
        prediction["{num}".format( num = 0)] = {'id_lead':int(ids[0]), 'prediction':int(predict[0])}
    else:
        for i, id_lead in enumerate(ids):
            prediction["{num}".format( num = int(i))] = {'id_lead':int(id_lead), 'prediction':int(predict[i])}

    return prediction


