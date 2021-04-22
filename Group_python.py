# 5Week Homework - Load Excel File

import openpyxl
import pandas as pd 

xlsxFile = '5week.xlsx' 
sheetList = [] 

wb = openpyxl.load_workbook(xlsxFile)
for i in wb.sheetnames: 
    sheetList.append(i)


