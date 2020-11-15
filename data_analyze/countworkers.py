import xlrd
from json import loads, dumps


def count_workers():
    rb = xlrd.open_workbook('input/Численность занятых 2005-2016.xlsx')
    sheet = rb.sheet_by_index(0)
    data = {}
    current = ""
    years = sheet.row_values(1)[2:]
    for rownum in range(sheet.nrows)[2:]:
        row = sheet.row_values(rownum)
        data[row[1]] = row[2:]
    return years, data


data = count_workers()[1]
print(*data.items(), sep="\n")
