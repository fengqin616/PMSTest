# -*- coding: utf-8 -*-

import allure

from common.ReadExcel.getTestData import *
from common.Biz.pmsKeyword import *

# class TestBillingRule(object):
#     def __init__(self, file):
#          # file =      #深圳湾24小多次进出
#         file = r'D:\pytest\PMS\testdata\hdw.xls'     #湛江华都汇计费规则
#         schema = {'caseID': '', 'plateNo': '', 'eventType': '', 'eventTime': '', 'expectedValue': ''}
#         plateFirstWord = '苏'
#         self.testData = TestData(file,schema,plateFirstWord).getTestDataTuple()

dataPath = conftest.dataPath
hdhFile ={'ruleName':'湛江华都汇计费规则','testFile':dataPath+'\hdh_billing.xls'}
szwFile ={'ruleName':'深圳湾24小时多次进出计费规则','testFile':dataPath+'\szw24Hour3.xls'}
hnrbFile ={'ruleName':'湖南日报计费规则','testFile':dataPath+'\hnrb_billing.xls'}

schema = {'caseID': '', 'plateNo': '', 'eventType': '', 'eventTime': '', 'expectedValue': ''}
plateFirstWord = '苏'

testFile = hdhFile
testData = TestData(testFile['testFile'],schema,plateFirstWord).getTestDataTuple()

@allure.feature(testFile['ruleName'])
@pytest.mark.parametrize('caseID,plateNo,eventType,eventTime,expectedValue',testData)
# @allure.step('执行测试用例')
def test_billingRule(caseID, plateNo, eventType, eventTime, expectedValue):

        # plateNo = plateNo.encode('utf-8').decode("unicode-escape")
        allure.attach(eventType+'    '+eventTime,plateNo)

        if eventType == '入场':
            PmsKeyWord().carEnter(plateNo,eventTime)

        if eventType == '计费':
            RealValue = PmsKeyWord().billing(plateNo,eventTime)
            assert RealValue == expectedValue

        if eventType == '出场':
            RealValue = PmsKeyWord().carExit(plateNo,eventTime)
            assert RealValue == expectedValue

