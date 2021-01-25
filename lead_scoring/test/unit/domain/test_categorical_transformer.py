from lead_scoring.domain.categorical_transformer import CategoricalTransformer
import pandas as pd

def test_categorical_transformer():
    cat_feat_clean = {
    "QUALITE_LEAD": "pourrait etre pertinent",
    "TAGS": "ne pas suivre de formation",
    "DERNIERE_ACTIVITE": "email ouvert",
    }

    df = pd.DataFrame(data=cat_feat_clean, index=[0])

    cat_trans = CategoricalTransformer()
    cat_trans = cat_trans.fit_transform(df)

    expected_values = ["pourrait etre pertinent", "other","email ouvert"]

    for i, column in enumerate(cat_trans.columns):
        assert cat_trans[column].values[0]==expected_values[i]

