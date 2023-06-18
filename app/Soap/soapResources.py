import sys

import logging

from app.resources import zpv_key, id_lpu, namespaces
import xml.etree.ElementTree as ET

ET.register_namespace('soapenv', namespaces['soapenv'])
ET.register_namespace('soap', namespaces['soap'])
ET.register_namespace('tem', namespaces['tem'])
ET.register_namespace('hub', namespaces['hub'])


def xmlCreateClaimForRefusal(patient, appointment):
    try:
        filepath = f'{sys.path[-1]}app/Soap/SoapResources/CreateClaimForRefusal.xml'
        logging.info(f"Open: {filepath}")
        tree = ET.parse(filepath)
        root = tree.getroot()
    except IOError:
        print("CreateClaimForRefusal.xml file open error!")
        return None

    idLpu = root.find('.//tem:idLpu', namespaces=namespaces)
    guid = root.find('.//tem:guid', namespaces=namespaces)

    idPat = root.find('.//tem:idPat', namespaces=namespaces)
    idAppointment = root.find('.//tem:idAppointment', namespaces=namespaces)

    idLpu.text = id_lpu
    guid.text = zpv_key

    idPat.text = patient
    idAppointment.text = appointment

    xml_str = ET.tostring(root, encoding='unicode')

    logging.info(xml_str)
    print(xml_str)

    return xml_str


def xmlGetAvaibleAppointments(patient, doctor, visit_start, visit_end):
    try:
        filepath = f'{sys.path[-1]}app/Soap/SoapResources/GetAvaibleAppointments.xml'
        tree = ET.parse(filepath)
        root = tree.getroot()
    except IOError:
        print("GetAvaibleAppointments.xml file open error!")
        return None

    idLpu = root.find('.//tem:idLpu', namespaces=namespaces)
    guid = root.find('.//tem:guid', namespaces=namespaces)

    idPat = root.find('.//tem:idPat', namespaces=namespaces)
    GetAvaibleAppointments = root.find('.//tem:GetAvaibleAppointments', namespaces=namespaces)
    idDoc = root.find('.//tem:idDoc', namespaces=namespaces)
    visitStart = root.find('.//tem:visitStart', namespaces=namespaces)
    visitEnd = root.find('.//tem:visitEnd', namespaces=namespaces)

    idLpu.text = id_lpu
    guid.text = zpv_key

    idDoc.text = doctor
    visitStart.text = visit_start
    visitEnd.text = visit_end

    if patient is not None:
        idPat.text = patient
    else:
        GetAvaibleAppointments.remove(idPat)

    xml_str = ET.tostring(root, encoding='unicode')

    logging.info(xml_str)
    print(xml_str)

    return xml_str


def xmlGetDoctorList(patient, specialization):
    try:
        filepath = f'{sys.path[-1]}app/Soap/SoapResources/GetDoctorList.xml'
        tree = ET.parse(filepath)
        root = tree.getroot()
    except IOError:
        print("GetDoctorList.xml file open error!")
        return None

    idLpu = root.find('.//tem:idLpu', namespaces=namespaces)
    guid = root.find('.//tem:guid', namespaces=namespaces)
    idHistory = root.find('.//tem:idHistory', namespaces=namespaces)

    idSpesiality = root.find('.//tem:idSpesiality', namespaces=namespaces)
    idPat = root.find('.//tem:idPat', namespaces=namespaces)
    GetDoctorList = root.find('.//tem:GetDoctorList', namespaces=namespaces)

    idLpu.text = id_lpu
    guid.text = zpv_key
    idHistory.text = '1'

    if specialization is not None:
        idSpesiality.text = specialization
    else:
        GetDoctorList.remove(idSpesiality)

    if patient is not None:
        idPat.text = patient
    else:
        GetDoctorList.remove(idPat)

    xml_str = ET.tostring(root, encoding='unicode')

    logging.info(xml_str)
    print(xml_str)

    return xml_str


def xmlGetPatientHistory(patient):
    try:
        filepath = f'{sys.path[-1]}app/Soap/SoapResources/GetPatientHistory.xml'
        tree = ET.parse(filepath)
        root = tree.getroot()
    except IOError:
        print("GetPatientHistory.xml file open error!")
        return None

    idLpu = root.find('.//tem:idLpu', namespaces=namespaces)
    guid = root.find('.//tem:guid', namespaces=namespaces)

    idPat = root.find('.//tem:idPat', namespaces=namespaces)

    idLpu.text = id_lpu
    guid.text = zpv_key

    idPat.text = patient

    xml_str = ET.tostring(root, encoding='unicode')

    logging.info(xml_str)
    print(xml_str)

    return xml_str


def xmlGetSpesialityList(patient):
    try:
        filepath = f'{sys.path[-1]}app/Soap/SoapResources/GetSpesialityList.xml'
        tree = ET.parse(filepath)
        root = tree.getroot()
    except IOError:
        print("GetSpesialityList.xml file open error!")
        return None

    idLpu = root.find('.//tem:idLpu', namespaces=namespaces)
    guid = root.find('.//tem:guid', namespaces=namespaces)

    idPat = root.find('.//tem:idPat', namespaces=namespaces)
    GetSpesialityList = root.find('.//tem:GetSpesialityList', namespaces=namespaces)

    idLpu.text = id_lpu
    guid.text = zpv_key

    if patient is not None:
        idPat.text = patient
    else:
        GetSpesialityList.remove(idPat)

    xml_str = ET.tostring(root, encoding='unicode')

    logging.info(xml_str)
    print(xml_str)

    return xml_str


def xmlGetWorkingTime(doctor, visit_start, visit_end):
    try:
        filepath = f'{sys.path[-1]}app/Soap/SoapResources/GetWorkingTime.xml'
        tree = ET.parse(filepath)
        root = tree.getroot()
    except IOError:
        print("GetWorkingTime.xml file open error!")
        return None

    idLpu = root.find('.//tem:idLpu', namespaces=namespaces)
    guid = root.find('.//tem:guid', namespaces=namespaces)

    idDoc = root.find('.//tem:idDoc', namespaces=namespaces)
    visitStart = root.find('.//tem:visitStart', namespaces=namespaces)
    visitEnd = root.find('.//tem:visitEnd', namespaces=namespaces)

    idLpu.text = id_lpu
    guid.text = zpv_key

    idDoc.text = doctor
    visitStart.text = visit_start
    visitEnd.text = visit_end

    xml_str = ET.tostring(root, encoding='unicode')

    logging.info(xml_str)
    print(xml_str)

    return xml_str


def xmlSearchTop10Patient(snils, birthday):
    try:
        filepath = f'{sys.path[-1]}app/Soap/SoapResources/SearchTop10Patient.xml'
        tree = ET.parse(filepath)
        root = tree.getroot()
    except IOError:
        print("SearchTop10Patient.xml file open error!")
        return None

    idLpu = root.find('.//tem:idLpu', namespaces=namespaces)
    guid = root.find('.//tem:guid', namespaces=namespaces)

    Birthday = root.find('.//hub:Birthday', namespaces=namespaces)
    Snils = root.find('.//hub:Snils', namespaces=namespaces)

    idLpu.text = id_lpu
    guid.text = zpv_key

    Birthday.text = birthday
    Snils.text = snils

    xml_str = ET.tostring(root, encoding='unicode')

    logging.info(xml_str)
    print(xml_str)

    return xml_str


def xmlSetAppointment(patient, appointment, appointmentPrev):
    try:
        filepath = f'{sys.path[-1]}app/Soap/SoapResources/SetAppointment.xml'
        tree = ET.parse(filepath)
        root = tree.getroot()
    except IOError:
        print("SetAppointment.xml file open error!")
        return None

    idLpu = root.find('.//tem:idLpu', namespaces=namespaces)
    guid = root.find('.//tem:guid', namespaces=namespaces)

    idPat = root.find('.//tem:idPat', namespaces=namespaces)
    SetAppointment = root.find('.//tem:SetAppointment', namespaces=namespaces)
    idAppointment = root.find('.//tem:idAppointment', namespaces=namespaces)
    idAppointmentPrev = root.find('.//tem:idAppointmentPrev', namespaces=namespaces)

    idLpu.text = id_lpu
    guid.text = zpv_key

    idAppointment.text = appointment
    idPat.text = patient

    if appointmentPrev is not None:
        idAppointmentPrev.text = appointmentPrev
    else:
        SetAppointment.remove(idAppointmentPrev)

    xml_str = ET.tostring(root, encoding='unicode')

    logging.info(xml_str)
    print(xml_str)

    return xml_str
