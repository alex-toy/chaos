# chaos-4

Project 3
---------

By Marieme Gueye & Alessio Rea

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




