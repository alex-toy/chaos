__all__ = ["config"]

import os
import yaml

ENVIRONMENT = os.getenv("YOTTA_ML3_CONFIGURATION_PATH")
this_dir = os.path.dirname(os.path.realpath(__file__))
print(this_dir)

if ENVIRONMENT:
    config_file_path = ENVIRONMENT
else:
    config_file_path = os.path.join(this_dir, "config_api.yml")


with open(config_file_path, 'r') as file_in:
    config = yaml.safe_load(file_in)
