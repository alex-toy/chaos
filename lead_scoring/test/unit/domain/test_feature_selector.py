from lead_scoring.domain.feature_selector import FeatureSelector
import lead_scoring.config.config as cf
import pandas as pd

def test_feature_selector():
    unique_lead_clean = {
    "QUALITE_LEAD": "pourrait etre pertinent",
    "TAGS": "ne pas suivre de formation",
    "DERNIERE_ACTIVITE": "email ouvert",
    "DUREE_SUR_SITEWEB": 0,
    "NB_VISITES": 0
    }
    df = pd.DataFrame(data=unique_lead_clean, index=[0])

    expected_cat_columns = ["QUALITE_LEAD","TAGS","DERNIERE_ACTIVITE"]
    expected_num_columns = ["DUREE_SUR_SITEWEB","NB_VISITES"]

    cat_feat = FeatureSelector(cf.CAT_FEAT)
    cat_feat = cat_feat.fit_transform(df)

    num_feat = FeatureSelector(cf.NUM_FEAT)
    num_feat = num_feat.fit_transform(df)

    for i, column in enumerate(cat_feat.columns):
        assert column==expected_cat_columns[i]
    
    for i, column in enumerate(num_feat.columns):
        assert column==expected_num_columns[i]

    

