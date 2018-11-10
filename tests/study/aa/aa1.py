import pytest
import requests

def aaLoginToken(host,uri='/Account/Login'):

    url = host+uri

    my_header = {'Content-Type':'application/json'}

    payload_login = {'OprtNo':'admin', 'Password':'das123', 'Subject':'PMS'}
    # payload_login = dict(OprtNo='admin',Password='das123',Subject='PMS')
    payload_login = dict(OprtNo='admin',Password='das123',Subject='PMS')


    # mySession = requests.session()
    # r = mySession.post(url, headers=my_header, json=payload_login)
    r = requests.post(url, headers=my_header, json=payload_login)
    # print(r.url)
    # print(r.status_code)
    # print(r.content)

    return r.json()['token']
