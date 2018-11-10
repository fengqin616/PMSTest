from    common.Biz.requestData import *

import pytest
import common.Biz.requestData
import conftest

class PmsKeyWord(object):
    def __init__(self):
        self.host = conftest.webHost
        self.entryPassageID = conftest.entryPassageID
        self.exitPassageID = conftest.exitPassageID
        self.token = getLoginToken(self.host)
        pass

    def carEnter(self,plateNo,enterTime):
        url = self.host+"/PassTest/VehicleEventInfo"
        enterEvent = dict(EventType=1,EventDate=enterTime,CouponAmount=0, WaitingTime=0)
        eventTypeList = [enterEvent]
        # payload = dict(PlateNo=plateNo, EventTypeList=eventTypeList, EntryPassageID="5059777928553272514",ExitPassgeID="5383314251850749232",Reliability=1,VehicleType=2)
        payload = dict(PlateNo=plateNo, EventTypeList=eventTypeList, EntryPassageID=self.entryPassageID,ExitPassgeID=self.exitPassageID,Reliability=1,VehicleType=2)

        print(url)
        print(payload)
        print(self.token)
        responseData = getResponseData(url,payload,self.token)
        print(responseData)
        return responseData['data']


    def carExit(self,plateNo,exitTime):
        url = self.host+"/PassTest/VehicleEventInfo"
        exitEvent =  dict(EventType=4,EventDate=exitTime,CouponAmount=0, WaitingTime=0)

        eventTypeList = [exitEvent]
        payload = dict(PlateNo=plateNo, EventTypeList=eventTypeList, EntryPassageID=self.entryPassageID,ExitPassgeID=self.exitPassageID,Reliability=1,VehicleType=2)
        print(url)
        print(payload)
        print(self.token)
        responseData = getResponseData(url,payload,self.token)
        print(responseData)
        # print(responseData['data'])
        return responseData['data'][0]['shouldAmount']


    def carParking(self,plateNo,enterTime,exitTime):

        url = self.host+"/PassTest/VehicleEventInfo"
        enterEvent = dict(EventType=1,EventDate=enterTime,CouponAmount=0, WaitingTime=0)
        exitEvent =  dict(EventType=4,EventDate=exitTime,CouponAmount=0, WaitingTime=0)

        eventTypeList = [enterEvent,exitEvent]
        payload = dict(PlateNo=plateNo, EventTypeList=eventTypeList, EntryPassageID="5059777928553272514",ExitPassgeID="5383314251850749232",Reliability=1,VehicleType=2)

        responseData = getResponseData(url,payload,self.token)
        # print(responseData)
        return responseData['data'][1]['shouldAmount']

    def billing(self,plateNo,billingTime):
        pass

    def charge(self,plateNo,chargeTime):
        pass

kw = PmsKeyWord();

kw.carEnter('苏CECD05','2018-9-30 7:00:00')
kw.carExit('苏CECD05','2018-9-30 8:00:00')

# PmsKeyWord().carExit('苏CECD04','2018-9-30 7:00:00')
# # print(kw.carParking('苏CECD08','2018-10-25  14:00:00','2018-10-25  16:00:00'))
