import xlrd
from json import loads, dumps

def generate_opportunities_and_without_work_json_file(y=2018):
    title = [("Вакансии", "opportunities"),
             ("Безработные", "without_work")]
    rb_list = [xlrd.open_workbook(f'input/{i[0]}НаКонец{y}.xlsx') for i in title]
    sheet_list = [rb.sheet_by_index(0) for rb in rb_list]
    for t, sheet in enumerate(sheet_list) :
        data = {}
        current = ""
        for rownum in range(sheet.nrows)[5:]:
            row = sheet.row_values(rownum)
            if row[0]:
                current = row[0]
                data[current] = {}
            else:
                data[current][row[1]] = row[2]

        with open(f"output/{title[t][1]}{y}.json", "w", encoding="utf8") as file:
            print(dumps(data), file=file)
        # print('-----------')


if __name__ == '__main__':
    generate_opportunities_and_without_work_json_file()