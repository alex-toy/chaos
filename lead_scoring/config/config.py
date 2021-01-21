import os
NAME_FILE = 'data.csv'
FULL_PATH_DATA = os.path.os.getcwd()   

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
DATA_DIR = os.path.join(REPO_DIR, 'data')
FILE_DATA = os.path.join(DATA_DIR, NAME_FILE)

OUTPUTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../output'))
OUTPUTS_MODELS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../models'))

PERF_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../lead_scoring_marieme_alessio/domain/perf.txt'))


_SAVED_FILENAME = '_processed_data.csv'
JL = '.joblib'

LOG_REG_SAVED_FILENAME = 'log_reg' + _SAVED_FILENAME
LOG_REG_MODEL_FILE = 'log_reg' + JL

KNN = 'knn'
KNN_SAVED_FILENAME = KNN + _SAVED_FILENAME
KNN_MODEL_FILE = KNN + JL

RF = 'rf'
RF_SAVED_FILENAME = RF + _SAVED_FILENAME
RF_MODEL_FILE = RF + JL

SVC = 'svc'
SVC_SAVED_FILENAME = SVC + _SAVED_FILENAME
SVC_MODEL_FILE = SVC + JL

GB = 'gb'
GB_SAVED_FILENAME = GB + _SAVED_FILENAME
GB_MODEL_FILE = GB + JL


INFO_LOG_FILE_NAME = 'lead_scoring_info_log.log'
DATA_DIR = os.path.join(REPO_DIR, 'logs')
FILE_LOG = os.path.join(DATA_DIR, INFO_LOG_FILE_NAME)
LOGGING_FORMAT = '[%(asctime)s][%(levelname)s][%(module)s] - %(message)s'
LOGGING_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
#FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'


#new column names :
ID_CLIENT = "ID_CLIENT"
ORIGINE_LEAD = "ORIGINE_LEAD"
SOURCE_LEAD = "SOURCE_LEAD"
NIVEAU_LEAD = "NIVEAU_LEAD"
QUALITE_LEAD = "QUALITE_LEAD"
CONTACT_PAR_MAIL = "CONTACT_PAR_MAIL"
CONTACT_PAR_TELEPHONE = "CONTACT_PAR_TELEPHONE"
STATUT_ACTUEL = "STATUT_ACTUEL"
TARGET = "TARGET"
NB_VISITES = "NB_VISITES"
DUREE_SUR_SITEWEB = "DUREE_SUR_SITEWEB"
NB_PAGES_VUES_PAR_VISITE = "NB_PAGES_VUES_PAR_VISITE"
DERNIERE_ACTIVITE = "DERNIERE_ACTIVITE"
DERNIERE_ACTIVITE_NOTABLE = "DERNIERE_ACTIVITE_NOTABLE"
PAYS = "PAYS"
VILLE = "VILLE"
SPECIALISATION = "SPECIALISATION"
TAGS = "TAGS"
INDEX_ACTIVITE = "INDEX_ACTIVITE"
INDEX_PROFIL = "INDEX_PROFIL"
SCORE_ACTIVITE = "SCORE_ACTIVITE"
SCORE_PROFIL = "SCORE_PROFIL"
ANNONCE_VUE = "ANNONCE_VUE"
MAGAZINE = "MAGAZINE"
ARTICLE_JOURNAL = "ARTICLE_JOURNAL"
FORUM = "FORUM"
JOURNAUX = "JOURNAUX"
PUB_DIGITALE = "PUB_DIGITALE"
RECOMMANDATION = "RECOMMANDATION"
C_ENT_PARLER_NS = "C_ENT_PARLER_NS"
SOUH_TU_REC_INFOS = "SOUH_TU_REC_INFOS"
SOUH_REC_MAJ_PROG = "SOUH_REC_MAJ_PROG"
SOUH_REC_MAJ_MP = "SOUH_REC_MAJ_MP"
SOUH_PAYER_CHEQUE = "SOUH_PAYER_CHEQUE"
SOUH_REC_COPIE_LB = "SOUH_REC_COPIE_LB"

PRED_COL_NAME = 'PREDICTION'
PRED_PROBA_COL_NAME = 'PREDICTED_PROBABILITY'
 

NEW_COL_NAMES_TRAIN = [
    ID_CLIENT,
    ORIGINE_LEAD,
    SOURCE_LEAD,
    NIVEAU_LEAD,
    QUALITE_LEAD,
    CONTACT_PAR_MAIL,
    CONTACT_PAR_TELEPHONE,
    STATUT_ACTUEL,
    TARGET,
    NB_VISITES,
    DUREE_SUR_SITEWEB,
    NB_PAGES_VUES_PAR_VISITE,
    DERNIERE_ACTIVITE,
    DERNIERE_ACTIVITE_NOTABLE,
    PAYS,
    VILLE,
    SPECIALISATION,
    TAGS,
    INDEX_ACTIVITE,
    INDEX_PROFIL,
    SCORE_ACTIVITE,
    SCORE_PROFIL,
    ANNONCE_VUE,
    MAGAZINE,
    ARTICLE_JOURNAL,
    FORUM,
    JOURNAUX,
    PUB_DIGITALE,
    RECOMMANDATION,
    C_ENT_PARLER_NS,
    SOUH_TU_REC_INFOS,
    SOUH_REC_MAJ_PROG,
    SOUH_REC_MAJ_MP,
    SOUH_PAYER_CHEQUE,
    SOUH_REC_COPIE_LB
]

NEW_COL_NAMES_PRED = [
    ID_CLIENT,
    ORIGINE_LEAD,
    SOURCE_LEAD,
    NIVEAU_LEAD,
    QUALITE_LEAD,
    CONTACT_PAR_MAIL,
    CONTACT_PAR_TELEPHONE,
    STATUT_ACTUEL,
    NB_VISITES,
    DUREE_SUR_SITEWEB,
    NB_PAGES_VUES_PAR_VISITE,
    DERNIERE_ACTIVITE,
    DERNIERE_ACTIVITE_NOTABLE,
    PAYS,
    VILLE,
    SPECIALISATION,
    TAGS,
    INDEX_ACTIVITE,
    INDEX_PROFIL,
    SCORE_ACTIVITE,
    SCORE_PROFIL,
    ANNONCE_VUE,
    MAGAZINE,
    ARTICLE_JOURNAL,
    FORUM,
    JOURNAUX,
    PUB_DIGITALE,
    RECOMMANDATION,
    C_ENT_PARLER_NS,
    SOUH_TU_REC_INFOS,
    SOUH_REC_MAJ_PROG,
    SOUH_REC_MAJ_MP,
    SOUH_PAYER_CHEQUE,
    SOUH_REC_COPIE_LB
]

COL_NAME_TRAIN = ['ID_CLIENT', 'ORIGINE_LEAD', 'SOURCE_LEAD', 'NIVEAU_LEAD',
       'QUALITE_LEAD', 'CONTACT_PAR_MAIL', 'CONTACT_PAR_TELEPHONE',
       'STATUT_ACTUEL', 'CONVERTI', 'NB_VISITES', 'DUREE_SUR_SITEWEB',
       'NB_PAGES_VUES_PAR_VISITE', 'DERNIERE_ACTIVITE',
       'DERNIERE_ACTIVITE_NOTABLE', 'PAYS', 'VILLE', 'SPECIALISATION', 'TAGS',
       'INDEX_ACTIVITE', 'INDEX_PROFIL', 'SCORE_ACTIVITE', 'SCORE_PROFIL',
       'ANNONCE_VUE', 'MAGAZINE', 'ARTICLE_JOURNAL', 'FORUM', 'JOURNAUX',
       'PUB_DIGITALE', 'RECOMMANDATION',
       'Comment avez-vous entendu parler de nous ?',
       'Souhaites-tu recevoir plus d\'infos sur notre cours ?',
       'Souhaites-tu recevoir des mises à jour sur nos programmes ?',
       'Souhaites-tu recevoir des mises à jour par message privé ?',
       'Souhaites-tu payer par chèque ?',
       'Souhaites-tu recevoir une copie de notre livre blanc ?']


import re

def clean_line(line) :
    e = re.compile('[éèê]')
    a = re.compile('[àâ]')
    u = re.compile('[û]')
    o = re.compile('[ô]')

    line = e.sub('e', line)
    line = a.sub('a', line)
    line = u.sub('u', line)
    line = o.sub('o', line)
    return line.lower().rstrip().lstrip()



#############################


use_qualite_lead = []
path =os.path.abspath(os.path.join(os.path.dirname(__file__), 'use_qualite_lead.txt'))
f = open(path, 'r') 
lines = f.readlines()
for line in lines: 
    line = clean_line(line)
    use_qualite_lead.append(line)

use_tags = []
path =os.path.abspath(os.path.join(os.path.dirname(__file__), 'use_tags.txt'))
f = open(path, 'r') 
lines = f.readlines()
for line in lines: 
    line = clean_line(line)
    use_tags.append(line)

use_der_act = []
path =os.path.abspath(os.path.join(os.path.dirname(__file__), 'use_der_act.txt'))
f = open(path, 'r') 
lines = f.readlines()
for line in lines: 
    line = clean_line(line)
    use_der_act.append(line)



CAT_FEAT = [QUALITE_LEAD, TAGS, DERNIERE_ACTIVITE]

use_lists = [
    use_qualite_lead,
    use_tags,
    use_der_act,
]

NUM_FEAT =[DUREE_SUR_SITEWEB, NB_VISITES]

FEATURES = CAT_FEAT + NUM_FEAT
COLS_TO_KEEP = FEATURES + [TARGET]