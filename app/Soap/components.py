from flask import session
import uuid
from app.resources import session_auth_keys, ROLE_PATIENT, ROLE_DOCTOR


def init_session():
    if 'id' not in session:
        session['id'] = uuid.uuid4()


def isAuthorizationPatient():
    if 'Auth' in session:
        if session['Auth']['Role'] == ROLE_PATIENT:
            return True
    return False


def isAuthorizationDoctor():
    if 'Auth' in session:
        if session['Auth']['Role'] == ROLE_DOCTOR:
            return True
    return False


def authorize(data, role):
    # if 'Auth' not in session:
    keys = data.keys()
    Auth = {}
    for k in keys:
        Auth[k] = data[k]
    Auth['Role'] = role
    session['Auth'] = Auth
    # else:
    #     session.pop('Auth')


def unAuthorize():
    if 'Auth' in session:
        session.pop('Auth')
