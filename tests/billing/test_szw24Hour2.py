# -*- coding: utf-8 -*-

import allure

from common.ReadExcel.getTestData import *
from common.Biz.pmsKeyword import *

file = r'D:\pytest\PMSTest\testdata\szw24Hour2.xls'
schema = {'caseID': '', 'plateNo': '', 'enterTime': '', 'exitTime': '', 'expectedValue': ''}
plateFirstWord = '苏'

testData = TestData(file,schema,plateFirstWord).getTestDataTuple()

@allure.feature('深圳湾24小时多次进出计费规则测试2')
@pytest.mark.parametrize('caseID,plateNo,enterTime,exitTime,expectedValue',testData)
# @allure.step('执行测试用例')
def test_szw24Hour(caseID, plateNo, enterTime, exitTime, expectedValue):

    allure.attach(plateNo+'  入场时间：'+enterTime+'      出场时间：'+exitTime,'')
    realValue = PmsKeyWord().carParking(plateNo,enterTime,exitTime)
    assert realValue == expectedValue
