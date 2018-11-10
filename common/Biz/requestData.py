import pytest
import requests
import json

def getLoginToken(host,uri='/Account/Login'):

    url = host+uri

    my_header = {'Content-Type':'application/json'}

    # payload_login = {'OprtNo':'admin', 'Password':'das123', 'Subject':'PMS'}
    payload_login = dict(OprtNo='admin',Password='das123',Subject='PMS')

    # mySession = requests.session()
    # r = mySession.post(url, headers=my_header, json=payload_login)
    r = requests.post(url, headers=my_header, json=payload_login)

    return r.json()['token']

def getSignedPayload(payload,apiKey,host,uri='/api/tools/makeSign'):

    url = host+uri

    my_header = {'Content-Type':'application/json'}

    payload = dict(json=payload,key=apiKey)

    r = requests.post(url, headers=my_header, json=payload)
    # print(r.url,'   ',r.status_code,'   ',r.content)
    return r.json()['data']     #待补充出错处理
    # return {"plateNo":"粤B826FR","sign" : "FBA47D26155C9CEEC32783C0A1505459"}

def getResponseData(url,payload,token=None):

    if token is None:
        my_header = {'Content-Type':'application/json'}
    else:
        my_header = {'Content-Type':'application/json','token':token}
    # mySession = requests.session()
    # r = mySession.post(url, headers=my_header, json=payload_login)
    r = requests.post(url, headers=my_header, json=payload)

    # print(r.status_code,r.url,r)
    return r.json()


# token = getLoginToken(host_wan)
# print(token)
#
# url = host_wan+"/PlateFirstWord/GetPlateFirstWord"
# payload ={'DictCode':'PlateFirstWord'}
# responsedata = getResponseData(url,payload,token)
# print(responsedata)
# print(responsedata['data'][1])

# payload = dict(plateNo='粤B826FR',sign='')
# strPayload = json.dumps(payload)
# print(strPayload)

#
# # payload = dict(json=payload,key=apiKey)
# signedPayload = getSignedPayload(strPayload,apiKey,host)
# print(signedPayload)
