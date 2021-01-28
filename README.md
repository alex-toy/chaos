# Yotta Project 3 - Machine Learning Production pipeline

By Marieme Gueye & Alessio Rea

==============================

You need to have Python 3.8.5 installed for this project

# Getting started

## 0. Clone this repository

```
$ git clone <this_project>
$ cd <this_project>
```

## 1. Setup your virtual environment and activate it

Goal : create a local virtual environment in the folder `./.venv/`.

- First: check your python3.8 version:

    ```
    $ python3.8 --version
    # examples of outputs:
    Python 3.8.2 :: Anaconda, Inc.
    Python 3.8.5

    $ which python3.8
    /Users/bin/anaconda3/bin/python3
    /usr/bin/python3
    ```

    - If you don't have python3.8 and you are working on your mac: install it from [python.org](https://www.python.org/downloads/)
    - If you don't have python3 and are working on an ubuntu-like system: install from package manager:

        ```
        $ apt-get update
        $ apt-get -y install python3.8 python3.8-pip python3.8-venv
        ```

- Now that python3.8 is installed create your environment, activate it and install necessary packages:

    ```
    $ source activate.sh
    ```

    You should **always** activate your environment when working on the project.

    It succeeds with the following message :

    ```
    ************************************************************************************
    Successfuly activated the virtual environment; you are now using this python:
    $(which python)
    ************************************************************************************
    ```

    If it fails with the following message :
    ```
    "ERROR: failed to activate virtual environment .venv! ask for advice on #dev "
    ```

## 2. Local use of API

Use two terminals.

- Open server:
    ```
    $ python chaos/lead_scoring/application/server.py #on terminal 1
    ```

You should see an IP (for instance: http://0.0.0.0:5000/)

- Make unitary churn prediction (NAME field not allowed in the app):
    ```
    curl -d '{"DERNIERE_ACTIVITE" : "Email ouvert", "DUREE_SUR_SITEWEB" : 10,  "NB_VISITES" : 10, "TAGS" : "Ne pas suivre de formation conti
    nue","QUALITE_LEAD" : "Pourrait être pertinent"}' -H "Content-Type: application/json" -X POST http://backend-api:5000/pred
    ```

It should return something like {"DERNIERE_ACTIVITE":"Email ouvert","DUREE_SUR_SITEWEB":10,"NB_VISITES":10,"QUALITE_LEAD":"Pourrait \u00eatre pertinent","TAGS":"Ne pas suivre de formation continue","predict_proba":0.13,"prediction":0}.

- Make several predictions from csv files:
    * Enter <IP>/predict-csv in your web browser.
    * Upload your csv file
    * Click "submit" and get your predictions download in a csv file with new column "CONVERTI"

## 3. Online use of API thanks to react frontend (TODO)




## 4. If you feel like updating source code & settings !

Your code will go in the folder `lead_scoring/config`.

You can change your settings (where data is stored, the names of features, the parameters of models...)
in `lead_scoring/config/`:
    - `config.py` should contain the configuration and env. variables you can change


## 5. Documentation for the API can be found there : 
https://web.postman.co/workspace/My-Workspace~bb9aa43a-ab99-4acc-89e3-6b1f5d15063d/request/14093288-ff12434f-8249-4de7-bfed-ba15ad0699a5


## 6. go to the frontend app there : 
http://34.77.115.125

# Project Organization 
----------------------

    ├── activate.sh
    ├── init.sh
    ├── README.md          <- The top-level README for users and developers using this project.
    ├── Dockerfile
    │
    ├── data          <- Directory to store data in.
    │
    ├── docs
    │   ├── make.bat
    │   ├── Makefile
    │   ├── source        <- Files to build documentation.
    │   └── build
    │       ├── toctrees
    │       └── html       <- HTML files to see the module documentation.
    │
    │
    ├── deployment           <- YAML files for deployment
    │   ├── deployment_api_template.yml       
    │   └── load_balancer.yml   
    │   └── server-cluster-ip.yml                       
    │
    │
    ├── models             <- Trained model.
    │
    ├── logs         <- logs from the code.
    │
    │
    ├── requirements.txt            <- Requirements for users.
    │
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so chaos can be imported
    ├── lead_scoring                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes chaos a Python module
    │   │
    │   ├── infrastructure           <- Scripts to load and clean data.
    │   │   ├── clean_data_transformer.py
    │   │   ├── connexion.py    
    │   │   ├── config
    │   │       ├── config.py
    │   │
    │   ├── config       <- User and developpers settings
    │   │   ├── config.py
    │   │
    │   ├── domain         <- Scripts to clean/create features and train model
    │   │   ├── categorical_transformer.py
    │   │   ├── customer.py
    │   │   └── feature_selector.py
    │   │
    │   ├── application     <- Churn JR App module
    │   │   ├── server.py
    │   │   └── gen_pikkle_file.py
    │   │
    │   ├── test        <- Unit and functional tests
    │   │   ├── functional
    │   │   └── unit


--------





