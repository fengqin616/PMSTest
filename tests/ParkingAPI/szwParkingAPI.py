import pytest
import allure
import sys


from common.ReadExcel.getTestData import *
from common.Biz.parkingAPI import *
import conftest

signHost = conftest.signHost
apiHost = conftest.apiHost
apiKey =conftest.apiKey

# @allure.feature('读取测试数据')
file = r'D:\pytest\PMS\testdata\szwParkingAPI.xls'
schema = {'caseID': '', 'plateNo': '', 'expectedValue': ''}

testData = TestData(file,schema).getTestDataTuple()
# print(testData)

@allure.feature('深圳湾查询计费测试')
@pytest.mark.parametrize('caseID,plateNo,expectedValue',testData)

def test_queryAndBilling(caseID, plateNo, expectedValue):

    # plateNo = plateNo.encode('utf-8').decode("unicode-escape")
    allure.attach(plateNo,'')

    response = ParkingAPI(signHost,apiKey,apiHost).queryAndBilling(plateNo)
    # print(response['status_code'],response)
    print(response)
    # assert realValue == expectedValue
    assert response['code'] == 51310  or response['code'] == 1

