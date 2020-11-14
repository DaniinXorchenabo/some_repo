import xlrd
from json import loads, dumps
rb = xlrd.open_workbook('Выпуск учреждений профобразования.xlsx')
sheet = rb.sheet_by_index(0)
data = {}
current = ""
years = sheet.row_values(2)[2:]
print(years)
for rownum in range(sheet.nrows)[3:]:
    row = sheet.row_values(rownum)
    if row[0]:
        current = row[0]
        data[current] = {}
    else:
        data[current][row[1]] = row[2:]
print(data)

with open("graduates.json", "w", encoding="utf8") as file:
    print(dumps(data), file=file)

