import requests
import json

from lead_scoring.infrastructure.config.config import config
from lead_scoring.test.unit.payload import unique_lead, multiple_lead

api = config["api"]
host = api["host"]
port = api["port"]


def test_preds_are_probabilities():
    endpoint = "preds"
    host = "0.0.0.0"
    port = 5000
    url = f"http://{host}:{port}/{endpoint}"
    
    headers = {'Content-Type': 'application/json' } 
    resp = requests.post(url, headers=headers, data=json.dumps(multiple_lead,indent=4))
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body["1"]['predict_proba'] >= 0
    assert resp_body["2"]['predict_proba'] <= 1



def test_pred_is_probability():
    endpoint = "pred"
    host = "0.0.0.0"
    port = 5000
    url = f"http://{host}:{port}/{endpoint}"
    
    headers = {'Content-Type': 'application/json' } 
    resp = requests.post(url, headers=headers, data=json.dumps(unique_lead,indent=4))
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['prediction'] >= 0
    assert resp_body['prediction'] <= 1