import xlrd
from json import loads, dumps

y = 2018
t = 1
title = [("Вакансии", "opportunities"),
         ("Безработные", "without_work")]
rb = xlrd.open_workbook(f'input/{title[t][0]}НаКонец{y}.xlsx')
sheet = rb.sheet_by_index(0)
data = {}
current = ""
for rownum in range(sheet.nrows)[5:]:
    row = sheet.row_values(rownum)
    if row[0]:
        current = row[0]
        data[current] = {}
    else:
        data[current][row[1]] = row[2]

with open(f"{title[t][1]}{y}.json", "w", encoding="utf8") as file:
    print(dumps(data), file=file)