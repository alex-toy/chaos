import os
from pathlib import Path
import pandas as pd

import lead_scoring.config.config as cf

import  pickle
import os
import pandas as pd
import csv


def test_model_file_exists():
    model = os.path.join(os.path.os.getcwd(), 'models/model_lead_scoring.pkl')
    assert os.path.isfile(model)