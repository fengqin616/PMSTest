import requests
import conftest
import pytest
import json


# @pytest.fixture
# def host():
#     return conftest.webHost

def test_Login(uri='/Account/Login'):
    host = conftest.webHost
    url = host+uri

    my_header = {'Content-Type':'application/json'}

    # payload_login = {'OprtNo':'admin', 'Password':'das123', 'Subject':'PMS'}
    payload_login = dict(OprtNo='admin',Password='das123',Subject='PMS')

    # mySession = requests.session()
    # r = mySession.post(url, headers=my_header, json=payload_login)
    r = requests.post(url, headers=my_header, json=payload_login)
    print(r.content)
    print(r.json()['token'])
    assert  r.status_code == 200


