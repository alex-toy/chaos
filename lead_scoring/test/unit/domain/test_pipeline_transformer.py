import lead_scoring.domain.pipeline_transformer as pt
import pandas as pd

def test_numerical_transformer():
    unique_lead_clean = {
    "QUALITE_LEAD": "pourrait etre pertinent",
    "TAGS": "ne pas suivre de formation",
    "DERNIERE_ACTIVITE": "email ouvert",
    "DUREE_SUR_SITEWEB": 30,
    "NB_VISITES": 70
    }

    df = pd.DataFrame(data=unique_lead_clean, index=[0])

    transformer = pt.pipeline_transformer()
    pipeline_transformer = transformer.fit_transform(df)

    #expected_values = [80,50]

    print(pipeline_transformer)

    #for i, column in enumerate(pipeline_transformer.columns):
     #   assert pipeline_transformer[column].values[0]==expected_values[i]




if __name__=="__main__":
    test_numerical_transformer()