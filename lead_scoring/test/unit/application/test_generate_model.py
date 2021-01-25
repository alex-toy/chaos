import os
from pathlib import Path
import pandas as pd

import lead_scoring.config.config as cf

import  pickle
import os
import pandas as pd
import csv
import sklearn


def test_model_file_exists():
    model_file_path = os.path.join(os.path.os.getcwd(), 'models/model_lead_scoring.pkl')
    _ , extension = os.path.splitext(model_file_path)

    assert os.path.isfile(model_file_path)
    assert extension=='.pkl'
    