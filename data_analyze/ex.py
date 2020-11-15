import xlrd
from json import loads, dumps
from os.path import join as os_join, isfile

path = ''


def generate_opportunities_and_without_work_json_file(y=2018):
    title = [("Вакансии", "opportunities"),
             ("Безработные", "without_work")]
    title = [(name, file_name, os_join(path, file_name)) for [name, file_name] in title]
    rb_list = [os_join(path, f'input/{i[0]}НаКонец{y}.xlsx') for i in title]
    rb_list = [xlrd.open_workbook(path) for path in rb_list if isfile(path) or print("Не удается найти файл!", path)]

    sheet_list = [rb.sheet_by_index(0) for rb in rb_list]
    for t, sheet in enumerate(sheet_list):
        data = {}
        current = ""
        for rownum in range(sheet.nrows)[5:]:
            row = sheet.row_values(rownum)
            if row[0]:
                current = row[0]
                data[current] = {}
            else:
                data[current][row[1]] = row[2]

        with open(os_join(path, f"output/{title[t][1]}{y}.json"), "w", encoding="utf8") as file:
            print(dumps(data), file=file)
        # print('-----------')


my_dir = "data_analyze"

if __name__ == '__main__':
    generate_opportunities_and_without_work_json_file()

else:
    from os import getcwd
    from os.path import split as os_split, exists, join as os_join

    path = getcwd()
    while my_dir not in path:
        if exists(os_join(path, my_dir)):
            path = os_join(path, my_dir)
            break
        now_dir = os_split(path)[1]
        path = os_split(path)[0]
        print(path, now_dir)
    else:
        all_path, end_dir = os_split(path)
        while end_dir != my_dir:
            now_dir = path[1]
            path = os_split(path[0])[0] if not bool(path[-1]) else path[0]
    print('end', path)
