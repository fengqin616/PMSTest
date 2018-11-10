# -*- coding: utf-8 -*-

import allure

from common.ReadExcel.getTestData import *
from common.Biz.pmsKeyword import *

file = r'D:\pytest\PMS\testdata\szw24Hour1.xls'
schema = {'caseID': '', 'plateNo': '', 'eventType': '', 'eventTime': '', 'expectedValue': ''}
plateFirstWord = '苏'

testData = TestData(file,schema,plateFirstWord).getTestDataTuple()

@allure.feature('深圳湾24小时多次进出计费规则测试')
@pytest.mark.parametrize('caseID,plateNo,eventType,eventTime,expectedValue',testData)
# @allure.step('执行测试用例')
def test_szw24Hour(caseID, plateNo, eventType, eventTime, expectedValue):

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

