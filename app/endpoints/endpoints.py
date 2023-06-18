from flask import request, Response, session
from app.Soap.components import init_session # импорт

headers = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "GET,PUT,POST,OPTIONS",
    "Access-Control-Allow-Methods": "*"
}

status = {
    "HTTP_200_OK": 200,
    "HTTP_415_UNSUPPORTED_MEDIA_TYPE": 415,
    "HTTP_400_BAD_REQUEST": 400
}


# endpoint: /
def root():
    init_session()

    return "Hello!"


# endpoint: /visits-counter/
def visits():
    init_session()

    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # чтение и обновление данных сессии
    else:
        session['visits'] = 1  # настройка данных сессии
    return "Total visits: {}".format(session.get('visits'))


def authorization():
    init_session()

    response = Response(status=status['HTTP_200_OK'], headers=headers)
    if 'role' in session:
        response = Response({"Вы уже авторизировались: {}".format(session['role'])},
                            status=status["HTTP_200_OK"],
                            headers=headers)
    else:
        if request.headers.get('Content-Type') == 'application/json':
            keys = request.json
            if keys.get('snils') != None and keys.get('birthday') != None:

                response = Response({"Ща авторизуем"},
                                    status=status["HTTP_200_OK"],
                                    headers=headers)
            else:
                response = Response({"Не хватает передаваемых параметров"},
                                    status=status["HTTP_400_BAD_REQUEST"],
                                    headers=headers)
        else:
            response = \
                Response(
                    {'Не передан тип передаваемых данных "application/json"'},
                    status=status["HTTP_415_UNSUPPORTED_MEDIA_TYPE"],
                    headers=headers)

    return response
