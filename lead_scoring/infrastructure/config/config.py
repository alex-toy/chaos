__all__ = ["config"]

import os
import yaml

this_dir = os.path.dirname(os.path.realpath(__file__))

# open config file for postgresql
ENVIRONMENT = os.getenv("YOTTA_ML3_CONFIGURATION_POSTGRE_PATH")
if ENVIRONMENT:
    config_file_path_pg = ENVIRONMENT
else:
    config_file_path_pg = os.path.join(this_dir, "config_pg.yml")

with open(config_file_path_pg, 'r') as file_in:
    config_pg = yaml.safe_load(file_in)

# open config file for api
config_file_path_api = os.path.join(this_dir, "config_api.yml")
with open(config_file_path_api, 'r') as file_in:
    config_api = yaml.safe_load(file_in)