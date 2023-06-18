import sys

sys.path.append('/app/')

from flask import Flask
from flask_cors import CORS

import logging
from endpoints.innerEndpoints import SearchTop10Patient, AuthPatient, GetSpesialityList, GetDoctorList, \
    GetAvaibleAppointments, SetAppointment, GetWorkingTime, GetPatientHistory, CreateClaimForRefusal, AuthDoctor # импорт
from resources import domain, secret_key, port

app = Flask(__name__)
ALLOWED_EXTENSIONS = ['json']
app.config['SESSION_COOKIE_MAX_AGE'] = 1
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


app.route('/inner/SearchTop10Patient', methods=['POST'])(SearchTop10Patient)
app.route('/inner/GetSpesialityList', methods=['POST'])(GetSpesialityList)
app.route('/inner/GetDoctorList', methods=['POST'])(GetDoctorList)
app.route('/inner/GetAvaibleAppointments', methods=['POST'])(GetAvaibleAppointments)
app.route('/inner/SetAppointment', methods=['POST'])(SetAppointment)
app.route('/inner/GetWorkingTime', methods=['POST'])(GetWorkingTime)
app.route('/inner/GetPatientHistory', methods=['POST'])(GetPatientHistory)
app.route('/inner/CreateClaimForRefusal', methods=['POST'])(CreateClaimForRefusal)
app.route('/inner/AuthDoctor', methods=['POST'])(AuthDoctor)
app.route('/inner/AuthPatient', methods=['POST'])(AuthPatient)

if __name__ == "__main__":
    logging.info("App run")
    try:

        app.secret_key = secret_key
        app.run(host=domain, port=port)


    except IOError:
        print("Resource file open error!")
        logging.error("Resource file open error!")
