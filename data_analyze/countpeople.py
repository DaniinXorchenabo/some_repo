import xlrd
from json import loads, dumps


def count_male():
    rb = xlrd.open_workbook('input/Численность населения по полу и возрасту Калининградской области 2015-2020.xls')
    data = {"male": {}, "female": {}}
    current = ""
    for si in range(5):

        sheet = rb.sheet_by_index(si)
        for rownum in range(sheet.nrows)[7:-4]:
            row = sheet.row_values(rownum)
            if "-" in row[0]:
                ad = 1 if si > 1 else 0
                data["male"][row[0]] = data["male"].get(row[0], []) + [row[2 + ad]]
                data["female"][row[0]] = data["female"].get(row[0], []) + [row[3 + ad]]

    return data
