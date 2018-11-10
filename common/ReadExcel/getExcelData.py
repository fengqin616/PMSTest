#coding:utf-8

import sys
import json

import xlrd

class   TestFile(object):
    def __init__(self,file,schema,sheet,startFlag='START',endFlag='END'):

        book = xlrd.open_workbook(file)

        if isinstance(sheet,int):
            self.sheet = book.sheet_by_index(sheet)
        else:
            self.sheet = book.sheet_by_name(sheet)

        self.startFlag = startFlag
        self.endFlag = endFlag

        self.start = self.__getXY(self.startFlag)
        self.end = self.__getXY(self.endFlag)

        self.schema = self.updateSchema(schema)

    def __getXY(self, flag):
        isMatching = False
        for j in range(0,self.sheet.ncols):
            for i in range(0,self.sheet.nrows):
                if  ( self.sheet.cell(i,j).ctype ==1 and flag in self.sheet.cell_value(i,j) ):
                    isMatching = True
                    break
            if isMatching:
                break
        return [i,j]


    # 获取指定区域的测试用例数据
    def updateSchema(self,schema):

        row = self.sheet.row_values(self.start[0]+1,self.start[1],self.end[1]+1)

        for colx in range(0,self.end[1]-self.start[1]+1):
            for key in schema.keys():
                if row[colx] == key:
                    schema[key]=colx
                    break
        return schema

    def getExcelData(self):

        excelData = self.schema.copy()
        excelDataList = []

        for rowx in range(self.start[0]+3,self.end[0]):

            row = self.sheet.row_values(rowx,self.start[1],self.end[1]+1)

            if str(row[0]) == '':   #第一列如为空，则视为空行，跳过
                continue

            for key in self.schema.keys():

                colx = self.schema[key]
                # print(key,colx)
                excelData[key] = row[colx]

            excelDataList.append(excelData.copy())

        return excelDataList

# file = r'D:\RF\szw24Hour2.xls'
# schema = {'plateNo':'','eventType':'','eventTime':'','expectedValue':''}
# #
# print TestFile(file,schema).GetExcelData()
