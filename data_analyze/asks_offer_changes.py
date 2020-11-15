from json import loads, dumps
from os.path import isfile

path = ""


def unsetBrackets(anydict):
    arrkeys = list(map(lambda x: x[:x.find("(") - 1], list(anydict.keys())))
    arr_values = list(anydict.values())
    temp = [(arrkeys[i], arr_values[i]) for i in range(len(arr_values))]
    return dict(temp)


def globalGetChanges(year, section, proposal_workless=False, job_opening=False):
    global path
    pathes = [os_join(path, str(f"output/without_work{year}.json")) if not proposal_workless else '',
              os_join(path, str(f"output/opportunities{year}.json")) if not job_opening else '']

    data = []
    for loc_path in filter(bool, pathes):
        if not isfile(loc_path):
            from data_analyze.ex import generate_opportunities_and_without_work_json_file
            generate_opportunities_and_without_work_json_file(year)
        if not isfile(loc_path):
            return dict(), dict()
        with open(loc_path, "r") as file:
            data.append(loads(file.read()))
    print(*data[0].keys(), sep='\n')
    data = [unsetBrackets(dat[section]) for dat in data]
    if job_opening or proposal_workless and len(data) > 1:
        return data[0]

    null_elements1 = set(data[0].keys()) - set(data[1].keys())  # элементы, которых нет во втором
    null_elements2 = set(data[1].keys()) - set(data[0].keys())  # элементы, которых нет в первом

    data[0].update({key: 0 for key in null_elements2})
    data[1].update({key: 0 for key in null_elements1})

    return data  # data_1{квалификация: количество}

def base_get_json_data():
    from datetime import date
    count = 0
    while True:
        year = date.today().year - count
        count += 1
        loc_path = os_join(path, str(f"output/without_work{year}.json"))
        if not isfile(loc_path):
            from data_analyze.ex import generate_opportunities_and_without_work_json_file
            generate_opportunities_and_without_work_json_file(year)
        if not isfile(loc_path):
            if count > 10:
                return []
            continue
        with open(loc_path, "r") as file:
            return loads(file.read())

def get_all_section():
    data = base_get_json_data()
    if bool(data):
        return list(data.keys())
    return  data


def get_qualifications_from_section(section, filt=lambda *a, **k: True):
    data = base_get_json_data()
    if bool(data):
        data = unsetBrackets(data[section])
        # print(*data, sep='\n')
        return list(filter(filt, data))
    return []

def get_years(max_deep_in_last=30):
    from datetime import date
    count = 0
    years = []
    while True:
        year = date.today().year - count
        count += 1
        loc_path = os_join(path, str(f"output/without_work{year}.json"))
        if not isfile(loc_path):
            from data_analyze.ex import generate_opportunities_and_without_work_json_file
            generate_opportunities_and_without_work_json_file(year)
        if not isfile(loc_path):
            if count > max_deep_in_last:
                break
            continue
        years.append(year)
    # print(years)
    return years

my_dir = "data_analyze"
if __name__ == '__main__':
    a = globalGetChanges(2018, section="РАЗДЕЛ F СТРОИТЕЛЬСТВО")
    print(a)
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
