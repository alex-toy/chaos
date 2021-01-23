from lead_scoring.infrastructure.clean_data_transformer import CleanDataTransformer
import pandas as pd
import lead_scoring.config.config as cf


def test_clean_data_tranformer():
    unique_lead = {
    "QUALITE_LEAD": "Pourrait être pertinent",
    "TAGS": "Ne pas suivre de formation continue",
    "DERNIERE_ACTIVITE": "Email ouvert",
    "DUREE_SUR_SITEWEB": 0,
    "NB_VISITES": 0
    }
    expected_columns=['QUALITE_LEAD', 'TAGS', 'DERNIERE_ACTIVITE', 'DUREE_SUR_SITEWEB','NB_VISITES']
    expected_value = ['pourrait etre pertinent', 'ne pas suivre de formation continue', 'email ouvert',0,0]
    df = pd.DataFrame(data=unique_lead, index=[0])

    cdt = CleanDataTransformer(is_train=False, df=df)
    df = cdt.load_cleaned_data()

    for i, column in enumerate(df.columns):
        assert column==expected_columns[i]
        assert df[column].values[0] == expected_value[i]

    