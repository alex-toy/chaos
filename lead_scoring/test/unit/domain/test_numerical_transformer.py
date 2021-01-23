from lead_scoring.domain.numerical_transformer import NumericalTransformer
import pandas as pd

def test_numerical_transformer():
    num_feat_clean = {
    "DUREE_SUR_SITEWEB": 80,
    "NB_VISITES": 70
    }

    df = pd.DataFrame(data=num_feat_clean, index=[0])

    num_trans = NumericalTransformer()
    num_trans = num_trans.fit_transform(df)

    expected_values = [80,50]

    for i, column in enumerate(num_trans.columns):
        assert num_trans[column].values[0]==expected_values[i]