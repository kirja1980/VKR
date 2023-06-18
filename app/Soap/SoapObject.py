import logging
import xml.etree.ElementTree as ET
import requests
from app.resources import zpv_url, zpv_host, errors, namespaces, ROLE_PATIENT
import app.Soap.soapResources as soapResources


class Soap(object):
    def CreateClaimForRefusal(self, patient, appointment):
        xml = soapResources.xmlCreateClaimForRefusal(patient, appointment)
        response = self.Soap(xml, "CreateClaimForRefusal")
        if 'Body' in response:
            root = ET.XML(response.get('Body'))

            Success_dom = root.find('.//hub:Success', namespaces=namespaces)
            if Success_dom != None:
                Success = True if Success_dom.text == 'true' else False

            else:
                Success = False

            if Success:
                result = {'Success': True}
            else:
                IdError_dom = root.findall('.//hub:IdError', namespaces=namespaces)
                ErrorDescription_dom = root.findall('.//hub:ErrorDescription', namespaces=namespaces)
                if len(IdError_dom) != 0 and len(IdError_dom) == len(ErrorDescription_dom):
                    error_arr = []
                    for index in range(len(IdError_dom)):
                        error_arr.append((int(IdError_dom[index].text), str(ErrorDescription_dom[index].text)))
                    result = {'Errors': error_arr}
                else:
                    result = {'IdError': 100,
                              'ErrorDescription': errors[100]}

                result['Success'] = False
        else:
            result = {'IdError': 200,
                      'ErrorDescription': errors[200],
                      'Success': False}
        return result

    def GetAvaibleAppointments(self, patient, doctor, visit_start, visit_end):
        xml = soapResources.xmlGetAvaibleAppointments(patient, doctor, visit_start, visit_end)
        response = self.Soap(xml, "GetAvaibleAppointments")
        if 'Body' in response:
            root = ET.XML(response.get('Body'))
            Success_dom = root.find('.//hub:Success', namespaces=namespaces)
            if Success_dom != None:
                Success = True if Success_dom.text == 'true' else False

            else:
                Success = False

            if Success:
                Appointment_array_dom = root.findall('.//hub:Appointment', namespaces=namespaces)
                AppointmentList = []
                for Appointment_dom in Appointment_array_dom:
                    AppointmentList.append(
                        {
                            "IdAppointment": Appointment_dom.find('.//hub:IdAppointment', namespaces=namespaces).text,
                            "Address": Appointment_dom.find('.//hub:Address', namespaces=namespaces).text,
                            "Num": Appointment_dom.find('.//hub:Num', namespaces=namespaces).text,
                            "Room": Appointment_dom.find('.//hub:Room', namespaces=namespaces).text,
                            "VisitEnd": Appointment_dom.find('.//hub:VisitEnd', namespaces=namespaces).text,
                            "VisitStart": Appointment_dom.find('.//hub:VisitStart', namespaces=namespaces).text
                        }
                    )
                result = {'AppointmentList': AppointmentList,
                          'Success': True}
            else:
                IdError_dom = root.findall('.//hub:IdError', namespaces=namespaces)
                ErrorDescription_dom = root.findall('.//hub:ErrorDescription', namespaces=namespaces)
                if len(IdError_dom) != 0 and len(IdError_dom) == len(ErrorDescription_dom):
                    error_arr = []
                    for index in range(len(IdError_dom)):
                        error_arr.append((int(IdError_dom[index].text), str(ErrorDescription_dom[index].text)))
                    result = {'Errors': error_arr}
                else:
                    result = {
                        'IdError': 100,
                        'ErrorDescription': errors[100]
                    }
                result['Success'] = False
        else:
            result = {
                'IdError': 200,
                'ErrorDescription': errors[200],
                'Success': False
            }
        return result

    def GetDoctorList(self, patient=None, specialization=None):
        xml = soapResources.xmlGetDoctorList(patient, specialization)
        response = self.Soap(xml, "GetDoctorList")
        if 'Body' in response:
            root = ET.XML(response.get('Body'))

            Success_dom = root.find('.//hub:Success', namespaces=namespaces)
            if Success_dom != None:
                Success = True if Success_dom.text == 'true' else False

            else:
                Success = False

            if Success:
                Doctor_array_dom = root.findall('.//hub:Doctor', namespaces=namespaces)
                DoctorList = []
                for Doctor_dom in Doctor_array_dom:
                    DoctorList.append(
                        {
                            "CountFreeParticipantIE": Doctor_dom.find('.//hub:CountFreeParticipantIE',
                                                                      namespaces=namespaces).text,
                            "CountFreeTicket": Doctor_dom.find('.//hub:CountFreeTicket', namespaces=namespaces).text,
                            "IdDoc": Doctor_dom.find('.//hub:IdDoc', namespaces=namespaces).text,
                            "LastDate": Doctor_dom.find('.//hub:LastDate', namespaces=namespaces).text,
                            "Name": Doctor_dom.find('.//hub:Name', namespaces=namespaces).text,
                            "NearestDate": Doctor_dom.find('.//hub:NearestDate', namespaces=namespaces).text,
                            "Snils": Doctor_dom.find('.//hub:Snils', namespaces=namespaces).text
                        }
                    )
                result = {'DoctorList': DoctorList,
                          'Success': True}
            else:
                IdError_dom = root.findall('.//hub:IdError', namespaces=namespaces)
                ErrorDescription_dom = root.findall('.//hub:ErrorDescription', namespaces=namespaces)
                if len(IdError_dom) != 0 and len(IdError_dom) == len(ErrorDescription_dom):
                    error_arr = []
                    for index in range(len(IdError_dom)):
                        error_arr.append((int(IdError_dom[index].text), str(ErrorDescription_dom[index].text)))
                    result = {'Errors': error_arr}
                else:
                    result = {
                        'IdError': 100,
                        'ErrorDescription': errors[100]
                    }
                result['Success'] = False
        else:
            result = {
                'IdError': 200,
                'ErrorDescription': errors[200],
                'Success': False
            }
        return result

    def GetPatientHistory(self, patient):
        xml = soapResources.xmlGetPatientHistory(patient)
        response = self.Soap(xml, "GetPatientHistory")
        if 'Body' in response:
            root = ET.XML(response.get('Body'))

            Success_dom = root.find('.//hub:Success', namespaces=namespaces)
            if Success_dom != None:
                Success = True if Success_dom.text == 'true' else False

            else:
                Success = False

            if Success:
                HistoryVisit_array_dom = root.findall('.//hub:HistoryVisit', namespaces=namespaces)
                HistoryVisitList = []
                for HistoryVisit_dom in HistoryVisit_array_dom:
                    HistoryVisitList.append(
                        {
                            "DateCreatedAppointment": HistoryVisit_dom.find('.//hub:DateCreatedAppointment',
                                                                            namespaces=namespaces).text,
                            "IdAppointment": HistoryVisit_dom.find('.//hub:IdAppointment', namespaces=namespaces).text,
                            "VisitStart": HistoryVisit_dom.find('.//hub:VisitStart', namespaces=namespaces).text,
                            "Name": HistoryVisit_dom.find('.//hub:Name', namespaces=namespaces).text,
                            "IdDoc": HistoryVisit_dom.find('.//hub:IdDoc', namespaces=namespaces).text,
                            "NameSpesiality": HistoryVisit_dom.find('.//hub:NameSpesiality', namespaces=namespaces).text
                        }
                    )

                HistoryRefusal_array_dom = root.findall('.//hub:HistoryRefusal', namespaces=namespaces)
                HistoryRefusalList = []
                for HistoryRefusal_dom in HistoryRefusal_array_dom:
                    HistoryRefusalList.append(
                        {
                            "DateCreatedAppointment": HistoryRefusal_dom.find('.//hub:DateCreatedAppointment',
                                                                              namespaces=namespaces).text,
                            "IdAppointment": HistoryRefusal_dom.find('.//hub:IdAppointment',
                                                                     namespaces=namespaces).text,
                            "VisitStart": HistoryRefusal_dom.find('.//hub:VisitStart', namespaces=namespaces).text,
                            "Name": HistoryRefusal_dom.find('.//hub:Name', namespaces=namespaces).text,
                            "IdDoc": HistoryRefusal_dom.find('.//hub:IdDoc', namespaces=namespaces).text,
                            "NameSpesiality": HistoryRefusal_dom.find('.//hub:NameSpesiality',
                                                                      namespaces=namespaces).text
                        }
                    )

                result = {'HistoryVisitList': HistoryVisitList,
                          'HistoryRefusalList': HistoryRefusalList,
                          'Success': True}
            else:
                IdError_dom = root.findall('.//hub:IdError', namespaces=namespaces)
                ErrorDescription_dom = root.findall('.//hub:ErrorDescription', namespaces=namespaces)
                if len(IdError_dom) != 0 and len(IdError_dom) == len(ErrorDescription_dom):
                    error_arr = []
                    for index in range(len(IdError_dom)):
                        error_arr.append((int(IdError_dom[index].text), str(ErrorDescription_dom[index].text)))
                    result = {'Errors': error_arr}
                else:
                    result = {
                        'IdError': 100,
                        'ErrorDescription': errors[100]
                    }
                result['Success'] = False
        else:
            result = {
                'IdError': 200,
                'ErrorDescription': errors[200],
                'Success': False
            }
        return result

    def GetSpesialityList(self, patient=None):
        xml = soapResources.xmlGetSpesialityList(patient)
        response = self.Soap(xml, "GetSpesialityList")
        if 'Body' in response:
            root = ET.XML(response.get('Body'))

            Success_dom = root.find('.//hub:Success', namespaces=namespaces)
            if Success_dom != None:
                Success = True if Success_dom.text == 'true' else False

            else:
                Success = False

            if Success:
                Spesiality_array_dom = root.findall('.//hub:Spesiality', namespaces=namespaces)
                SpesialityList = []
                for Spesiality_dom in Spesiality_array_dom:
                    SpesialityList.append(
                        {
                            "CountFreeParticipantIE": Spesiality_dom.find('.//hub:CountFreeParticipantIE',
                                                                          namespaces=namespaces).text,
                            "CountFreeTicket": Spesiality_dom.find('.//hub:CountFreeTicket',
                                                                   namespaces=namespaces).text,
                            "FerIdSpesiality": Spesiality_dom.find('.//hub:FerIdSpesiality',
                                                                   namespaces=namespaces).text,
                            "IdSpesiality": Spesiality_dom.find('.//hub:IdSpesiality', namespaces=namespaces).text,
                            "LastDate": Spesiality_dom.find('.//hub:LastDate', namespaces=namespaces).text,
                            "NameSpesiality": Spesiality_dom.find('.//hub:NameSpesiality', namespaces=namespaces).text,
                            "NearestDate": Spesiality_dom.find('.//hub:NearestDate', namespaces=namespaces).text
                        }
                    )
                result = {'SpesialityList': SpesialityList,
                          'Success': True}
            else:
                IdError_dom = root.findall('.//hub:IdError', namespaces=namespaces)
                ErrorDescription_dom = root.findall('.//hub:ErrorDescription', namespaces=namespaces)
                if len(IdError_dom) != 0 and len(IdError_dom) == len(ErrorDescription_dom):
                    error_arr = []
                    for index in range(len(IdError_dom)):
                        error_arr.append((int(IdError_dom[index].text), str(ErrorDescription_dom[index].text)))
                    result = {'Errors': error_arr}
                else:
                    result = {
                        'IdError': 100,
                        'ErrorDescription': errors[100]
                    }
                result['Success'] = False
        else:
            result = {
                'IdError': 200,
                'ErrorDescription': errors[200],
                'Success': False
            }
        return result

    def GetWorkingTime(self, doctor, visit_start, visit_end):
        xml = soapResources.xmlGetWorkingTime(doctor, visit_start, visit_end)
        response = self.Soap(xml, "GetWorkingTime")
        if 'Body' in response:
            root = ET.XML(response.get('Body'))

            Success_dom = root.find('.//hub:Success', namespaces=namespaces)
            if Success_dom != None:
                Success = True if Success_dom.text == 'true' else False

            else:
                Success = False

            if Success:
                WorkingTime_array_dom = root.findall('.//hub:WorkingTime', namespaces=namespaces)
                WorkingTimeList = []
                for WorkingTime_dom in WorkingTime_array_dom:
                    WorkingTimeList.append(
                        {
                            "DenyCause": WorkingTime_dom.find('.//hub:DenyCause', namespaces=namespaces).text,
                            "RecordableDay": WorkingTime_dom.find('.//hub:RecordableDay', namespaces=namespaces).text,
                            "VisitStart": WorkingTime_dom.find('.//hub:VisitStart', namespaces=namespaces).text,
                            "VisitEnd": WorkingTime_dom.find('.//hub:VisitEnd', namespaces=namespaces).text
                        }
                    )
                result = {'WorkingTimeList': WorkingTimeList,
                          'Success': True}
            else:
                IdError_dom = root.findall('.//hub:IdError', namespaces=namespaces)
                ErrorDescription_dom = root.findall('.//hub:ErrorDescription', namespaces=namespaces)
                if len(IdError_dom) != 0 and len(IdError_dom) == len(ErrorDescription_dom):
                    error_arr = []
                    for index in range(len(IdError_dom)):
                        error_arr.append((int(IdError_dom[index].text), str(ErrorDescription_dom[index].text)))
                    result = {'Errors': error_arr}
                else:
                    result = {
                        'IdError': 100,
                        'ErrorDescription': errors[100]
                    }
                result['Success'] = False
        else:
            result = {
                'IdError': 200,
                'ErrorDescription': errors[200],
                'Success': False
            }
        return result

    def SearchTop10Patient(self, snils, birthday):
        xml = soapResources.xmlSearchTop10Patient(snils, birthday)
        response = self.Soap(xml, "SearchTop10Patient")
        if 'Body' in response:
            root = ET.XML(response.get('Body'))

            Success_dom = root.find('.//hub:Success', namespaces=namespaces)
            if Success_dom != None:
                Success = True if Success_dom.text == 'true' else False
            else:
                Success = False

            if Success:
                AriaNumber_dom = root.find('.//hub:AriaNumber', namespaces=namespaces)
                Birthday_dom = root.find('.//hub:Birthday', namespaces=namespaces)
                CellPhone_dom = root.find('.//hub:CellPhone', namespaces=namespaces)
                Document_N_dom = root.find('.//hub:Document_N', namespaces=namespaces)
                Document_S_dom = root.find('.//hub:Document_S', namespaces=namespaces)
                IdPat_dom = root.find('.//hub:IdPat', namespaces=namespaces)
                Name_dom = root.find('.//hub:Name', namespaces=namespaces)
                SecondName_dom = root.find('.//hub:SecondName', namespaces=namespaces)
                Surname_dom = root.find('.//hub:Surname', namespaces=namespaces)
                Snils_dom = root.find('.//hub:Snils', namespaces=namespaces)
                result = {
                    'AriaNumber': AriaNumber_dom.text,
                    'Birthday': Birthday_dom.text,
                    'CellPhone': CellPhone_dom.text,
                    'Document_N': Document_N_dom.text,
                    'Document_S': Document_S_dom.text,
                    'IdPat': IdPat_dom.text,
                    'Name': Name_dom.text,
                    'SecondName': SecondName_dom.text,
                    'Surname': Surname_dom.text,
                    'Snils': Snils_dom.text,
                    'Success': True
                }
            else:
                IdError_dom = root.findall('.//hub:IdError', namespaces=namespaces)
                ErrorDescription_dom = root.findall('.//hub:ErrorDescription', namespaces=namespaces)
                if len(IdError_dom) != 0 and len(IdError_dom) == len(ErrorDescription_dom):
                    error_arr = []
                    for index in range(len(IdError_dom)):
                        error_arr.append((int(IdError_dom[index].text), str(ErrorDescription_dom[index].text)))
                    result = {'Errors': error_arr}
                else:
                    result = {
                        'IdError': 100,
                        'ErrorDescription': errors[100]
                    }
                result['Success'] = False
        else:
            result = {
                'IdError': 200,
                'ErrorDescription': errors[200],
                'Success': False
            }
        return result

    def SetAppointment(self, patient, appointment, appointmentPrev):
        xml = soapResources.xmlSetAppointment(patient, appointment, appointmentPrev)
        response = self.Soap(xml, "SetAppointment")
        if 'Body' in response:
            root = ET.XML(response.get('Body'))

            Success_dom = root.find('.//hub:Success', namespaces=namespaces)
            if Success_dom != None:
                Success = True if Success_dom.text == 'true' else False

            else:
                Success = False

            if Success:
                Type = root.find('.//hub:Type', namespaces=namespaces)

                result = {'Type': Type.text,
                          'Success': True}
            else:
                IdError_dom = root.findall('.//hub:IdError', namespaces=namespaces)
                ErrorDescription_dom = root.findall('.//hub:ErrorDescription', namespaces=namespaces)
                if len(IdError_dom) != 0 and len(IdError_dom) == len(ErrorDescription_dom):
                    error_arr = []
                    for index in range(len(IdError_dom)):
                        error_arr.append((int(IdError_dom[index].text), str(ErrorDescription_dom[index].text)))
                    result = {'Errors': error_arr}
                else:
                    result = {
                        'IdError': 100,
                        'ErrorDescription': errors[100]
                    }
                result['Success'] = False
        else:
            result = {
                'IdError': 200,
                'ErrorDescription': errors[200],
                'Success': False
            }
        return result

    def headers(self, body, SOAPAction):
        headers = {'Content-Length': str(len(body)),
                   'Host': zpv_host,
                   'Content-Type': 'text/xml; charset=utf-8'}
        if SOAPAction is not None:
            headers['SOAPAction'] = f"http://tempuri.org/IHubService/{SOAPAction}"
        return headers

    def Soap(self, body, SOAPAction=None):
        response_root = None
        try:
            headers = self.headers(body, SOAPAction)
            response = requests.post(zpv_url, data=body, headers=headers)

            if response.ok:
                response_root = {"Body": response.text}
            else:
                response_root = {"Error": str(response.status_code)}

            logging.info(response_root)
            print(response_root)

        except Exception as e:
            logging.error(e)
            print(e)
        return response_root
