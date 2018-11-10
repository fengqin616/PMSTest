#coding=utf-8

import time
from common.ReadExcel.getExcelData import *

class TestData(object):
    def __init__(self,file,schema,plateFirstWord='',sheet=0):
        self.file = file
        self.sheet = sheet
        self.schema = schema
        self.plateFirstWord = plateFirstWord

    def __intToChr(self, i):
        if i < 10:
            return str(int(i))
        else:
            return chr(55 + int(i))

    def __getPlateHead(self):
        plateHead = [self.plateFirstWord, '', '', '', '']

        day    = time.localtime().tm_mday
        hour   = time.localtime().tm_hour
        minute = time.localtime().tm_min
        second    = time.localtime().tm_sec

        if hour>=8:
            plateHead[1]=chr(65 + hour-8)
        else:
            plateHead[1]=chr(65 + hour+16)

        plateHead[2] = self.__intToChr(day)

        #超过三秒，产生的plateHead会不一样
        plateHead[3] = self.__intToChr((minute * 20 + second / 3) / 36)
        plateHead[4] = self.__intToChr((minute * 20 + second / 3) % 36)

        plateHead = ''.join(plateHead)
        return plateHead  #.encode('UTF-8')


    def __getPlateNo(self, plate):
        if len(self.plateFirstWord) == 0: #首字母为空，则测试数据中的车牌已经是全车牌
            return plate
        else:                               #首字母非空，则测试数据中的车牌代表车牌尾部
            if isinstance(plate,float):
                plateTail =str(int(plate))
            else:
                plateTail = plate

        if len(plateTail) == 1 :
            plateTail = '0'+plateTail

        plateHead = self.__getPlateHead()  #.decode('UTF-8', 'strict')
        plateNo = plateHead + plateTail

        return plateNo


    def getTestData(self):

        myExcelFile =  TestFile(self.file, self.schema,self.sheet)

        testDataList = []

        for testData in myExcelFile.getExcelData():

            testData['plateNo'] = self.__getPlateNo(testData['plateNo'])

            testDataList.append(testData.copy())

        return testDataList


    def getTestDataTuple(self):

        testDataList =[]
        for testData in self.getTestData():
            testData['caseID'] = int(testData['caseID'])
            # testDataItem['plateNo'] = testDataItem['plateNo']

            testDataTuple = tuple(testData.values())
            testDataList.append(testDataTuple)

        return testDataList


# file = r'D:\pytest\PMS\testdata\szw24Hour1.xls'
# schema = {'caseID':'','plateNo':'','eventType':'','eventTime':'','expectedValue':''}
# plateFirstWord = '苏'
#
# print(TestData(file,schema,plateFirstWord).getTestData())
# print(TestData(file,schema,plateFirstWord).getTestDataTuple())
