import os
import chaos
from chaos.application.server import pred
from chaos.test.unit.payload import unique_lead, multiple_lead
import requests
import json
import requests_mock
from pathlib import Path
from flask import Flask, jsonify, request



def test_model_file_exists():
    model = os.path.join(chaos.__path__[0], "domain/model.pkl")
    assert os.path.isfile(model)







