import xlrd
import string

def Read_Entire_Excel_Using_Xlrd(FileName, WorksheetName):
    workbook = xlrd.open_workbook(FileName, on_demand = True)
    worksheet = workbook.sheet_by_name(WorksheetName)
    first_row = []
    for col in range(worksheet.ncols):
        first_row.append( worksheet.cell_value(0,col) )
    # Stores Cell's Data to a list of dictionaries
    DataFromExcel =[]
    for row in range(1, worksheet.nrows):
        colDic = {}
        for col in range(worksheet.ncols):
            colDic[first_row[col]]=worksheet.cell_value(row,col)
        DataFromExcel.append(colDic)
    return DataFromExcel

