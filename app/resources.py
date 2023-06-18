domain = '0.0.0.0'
port = '5000'
secret_key = 'e04f99ee-6d7a-4c0b-b70a-cc2d53c61b3a'
zpv_host = 'r47-rc.zdrav.netrika.ru'
zpv_url = 'http://r47-rc.zdrav.netrika.ru/hub25/HubService.svc'
# zpv_host = 'localhost'
# zpv_url = 'http://localhost/1C_ZPV/ws/appointment/'
zpv_key = 'b3ea4e5f-56e1-4205-abf0-35a3394457ee'
id_lpu = '30'
errors = {100: 'Произошла ошибка вызова',
          200: 'Произошла подключения к сервису'}
cors_headers = {
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Origin': '*',
    'Content-Type': 'application/json'
}
namespaces = {'hub': 'http://schemas.datacontract.org/2004/07/HubService2',
              'soapenv': "http://schemas.xmlsoap.org/soap/envelope/",
              'soap': "http://schemas.xmlsoap.org/soap/envelope/",
              'tem': "http://tempuri.org/"}
ROLE_PATIENT = 'PATIENT'
ROLE_DOCTOR = 'DOCTOR'
ROLE_MEDICAL_ORGANIZATION = 'MEDICAL_ORGANIZATION'
session_auth_keys = ['Role', 'AriaNumber', 'Birthday', 'CellPhone', 'Document_N', 'Document_S', 'IdPat', 'Name',
                     'SecondName', 'Surname', 'Snils']
