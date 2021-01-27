# Yotta Project 3 - ML in prod - Chaos

By Marieme Gueye & Alessio Rea

==============================

You need to have Python 3.8 installed for this project 
Simply use command from project root directory :

```bash
source activate.sh
```

It will :

-create a virtual environment and install all dependencies


Test the prediction locally
---------------------------

To run the server locally, execute the following command

```bash
python chaos/lead_scoring/application/server.py
```
It will run the server on http://0.0.0.0:5000/

Try to get an prediction probability with the following command:
```
curl -d '{"DERNIERE_ACTIVITE" : "Email ouvert", "DUREE_SUR_SITEWEB" : 10,  "NB_VISITES" : 10, "TAGS" : "Ne pas suivre de formation conti
nue","QUALITE_LEAD" : "Pourrait être pertinent"}' -H "Content-Type: application/json" -X POST http://backend-api:5000/pred
```






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
    /Users/benjamin/anaconda3/bin/python3
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

    You sould **allways** activate your environment when working on the project.

    If it fails with one of the following message :
    ```
    "ERROR: failed to create the .venv : do it yourself!"
    ```

## 2. Local use of API

Use two terminals.

- Open server:
    ```
    $ python chaos/application/server.py #on terminal 1
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
    * Upload your csv files (order of files matter!)
    * Click "Envoyer" button and see your predictions download in a csv file

## 3. Online use of API thanks to react frontend (TODO)




## 4. If you feel like updating source code & settings !

Your code will go in the folder `lead_scoring/config`.

You can change your settings (where data is stored, the names of features, the parameters of models...)
in `chaos/config/`:
    - `config.py` should contain the configuration and env. variables you can change


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





