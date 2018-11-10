from    common.Biz.requestData import *

import pytest
import common.Biz.requestData

class ParkingAPI():
    def __init__(self,sighHost,key,apiHost):

        self.sighHost = sighHost
        self.apiHost = apiHost
        self.key = key

    def queryAndBilling(self,plateNo):
        payload = dict(plateNo=plateNo,sign='')
        strPayload = json.dumps(payload)
        signedPayload = getSignedPayload(strPayload,self.key,self.sighHost)

        signedPayload = json.loads(signedPayload)

        uri = '/api/parking/queryAndBilling'
        url =self.apiHost+uri
        return getResponseData(url,signedPayload)


