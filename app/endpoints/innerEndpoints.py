import http
import json

from Soap import SoapObject
from flask import request, Response, session  # импорт
from app.resources import cors_headers, ROLE_PATIENT, ROLE_DOCTOR
from app.Soap.components import init_session, authorize, isAuthorizationPatient, isAuthorizationDoctor, unAuthorize  # импорт

soap = SoapObject.Soap()


def SearchTop10Patient():
    init_session()

    keys = request.json
    body = soap.SearchTop10Patient(keys.get('snils'), keys.get('birthday'))

    if isAuthorizationDoctor():
        if session['Auth']['Role'] != ROLE_DOCTOR:
            return Response({}, status=http.HTTPStatus.UNAUTHORIZED, headers=cors_headers)
        if body['Success']:
            return_body = body
            return_body.pop('Success')
            return Response(json.dumps(return_body), status=http.HTTPStatus.OK, headers=cors_headers)

    return Response(json.dumps({}), status=http.HTTPStatus.UNAUTHORIZED, headers=cors_headers)


def GetSpesialityList():
    init_session()

    if isAuthorizationPatient():
        body = soap.GetSpesialityList(session['Auth']['IdPat'])
    else:
        body = soap.GetSpesialityList()

    return Response(json.dumps(body), status=http.HTTPStatus.OK, headers=cors_headers)


def GetDoctorList():
    init_session()

    keys = request.json
    if isAuthorizationPatient():
        body = soap.GetDoctorList(session['Auth']['IdPat'], keys.get('spesiality'))
    else:
        body = soap.GetDoctorList(None, keys.get('spesiality'))

    return Response(json.dumps(body), status=http.HTTPStatus.OK, headers=cors_headers)


def GetAvaibleAppointments():
    init_session()

    keys = request.json
    if isAuthorizationPatient():
        body = soap.GetAvaibleAppointments(session['Auth']['IdPat'], keys.get('doctor'), keys.get('visit_start'),
                                           keys.get('visit_end'))
    else:
        body = soap.GetAvaibleAppointments(None, keys.get('doctor'), keys.get('visit_start'), keys.get('visit_end'))

    return Response(json.dumps(body), status=http.HTTPStatus.OK, headers=cors_headers)


def SetAppointment():
    init_session()

    keys = request.json
    if isAuthorizationPatient():
        body = soap.SetAppointment(session['Auth']['IdPat'], keys.get('appointment'), keys.get('appointmentPrev'))

        return Response(json.dumps(body), status=http.HTTPStatus.OK, headers=cors_headers)
    return Response(json.dumps({}), status=http.HTTPStatus.UNAUTHORIZED, headers=cors_headers)


def GetWorkingTime():
    init_session()

    keys = request.json
    if isAuthorizationPatient():
        body = soap.GetWorkingTime(keys.get('doctor'), keys.get('visit_start'), keys.get('visit_end'))
    else:
        body = soap.GetWorkingTime(keys.get('doctor'), keys.get('visit_start'), keys.get('visit_end'))

    return Response(json.dumps(body), status=http.HTTPStatus.OK, headers=cors_headers)


def GetPatientHistory():
    init_session()

    if isAuthorizationPatient():
        body = soap.GetPatientHistory(session['Auth']['IdPat'])

        return Response(json.dumps(body), status=http.HTTPStatus.OK, headers=cors_headers)
    return Response(json.dumps({}), status=http.HTTPStatus.UNAUTHORIZED, headers=cors_headers)


def CreateClaimForRefusal():
    init_session()

    keys = request.json
    if isAuthorizationPatient():
        body = soap.CreateClaimForRefusal(session['Auth']['IdPat'], keys.get('appointment'))

        return Response(json.dumps(body), status=http.HTTPStatus.OK, headers=cors_headers)
    return Response(json.dumps({}), status=http.HTTPStatus.UNAUTHORIZED, headers=cors_headers)


# Далее свои функции

def AuthDoctor():
    init_session()

    keys = request.json
    if isAuthorizationDoctor():
        return_body = {"Name": session['Auth']['Name'],
                       "Success": True}
        return Response(json.dumps(return_body), status=http.HTTPStatus.OK, headers=cors_headers)
    else:
        body = soap.GetDoctorList(None, None)
        if body.get('Success'):
            for doctor in body['DoctorList']:
                if ''.join(i for i in keys['snils'] if i.isdigit()) ==\
                        ''.join(i for i in doctor['Snils'] if i.isdigit()):
                    authorize(doctor, ROLE_DOCTOR)

    if isAuthorizationDoctor():
        return_body = {"Name": session['Auth']['Name'],
                       "Success": True}
        return Response(json.dumps(return_body), status=http.HTTPStatus.OK, headers=cors_headers)

    return Response(json.dumps({"Success": False,
                                "Error": "Ошибка аутентификации!"}), status=http.HTTPStatus.OK, headers=cors_headers)


def AuthPatient():
    init_session()
    unAuthorize()

    if isAuthorizationPatient():
        return_body = {
            'Snils': session['Auth']['Snils'],
            'Name': session['Auth']['Name'],
            'SecondName': session['Auth']['SecondName'],
            'Surname': session['Auth']['Surname'],
            'Success': True
        }
        return Response(json.dumps(return_body), status=http.HTTPStatus.OK, headers=cors_headers)

    keys = request.json
    body = soap.SearchTop10Patient(keys.get('snils'), keys.get('birthday'))
    if body.get('Success'):
        authorize(body, ROLE_PATIENT)

    if isAuthorizationPatient():
        return_body = {
            'Snils': session['Auth']['Snils'],
            'Name': session['Auth']['Name'],
            'SecondName': session['Auth']['SecondName'],
            'Surname': session['Auth']['Surname'],
            'Success': True
        }
        return Response(json.dumps(return_body), status=http.HTTPStatus.OK, headers=cors_headers)

    return Response(json.dumps({"Success": False,
                                "Error": "Ошибка аутентификации!"}), status=http.HTTPStatus.OK, headers=cors_headers)
