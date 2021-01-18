import os
import chaos
from chaos.application.server import pred
from chaos.test.unit.payload import unique_lead, multiple_lead
import requests
import json
import requests_mock
from pathlib import Path
from flask import Flask, jsonify, request


def test_preds_are_probabilities():
    url = 'http://0.0.0.0:5000/preds'
    
    headers = {'Content-Type': 'application/json' } 
    resp = requests.post(url, headers=headers, data=json.dumps(multiple_lead,indent=4))
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body["1"]['predict_proba'] >= 0
    assert resp_body["2"]['predict_proba'] <= 1



def test_pred_is_probability():
    url = 'http://0.0.0.0:5000/pred'
    
    headers = {'Content-Type': 'application/json' } 
    resp = requests.post(url, headers=headers, data=json.dumps(unique_lead,indent=4))
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['prediction'] >= 0
    assert resp_body['prediction'] <= 1


