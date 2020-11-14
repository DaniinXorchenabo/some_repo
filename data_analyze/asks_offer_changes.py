from json import loads, dumps
from os.path import isfile

path = ""


def unsetBrackets(anydict):
    arrkeys = list(map(lambda x: x[:x.find("(") - 1], list(anydict.keys())))
    arr_values = list(anydict.values())
    temp = [(arrkeys[i], arr_values[i]) for i in range(len(arr_values))]
    return dict(temp)


def globalGetChanges(year, section):
    file_asks = os_join(path, str(f"output/without_work{year}.json"))
    file_offer = os_join(path, str(f"output/opportunities{year}.json"))
    if not isfile(file_asks):
        from data_analyze.ex import generate_opportunities_and_without_work_json_file
        generate_opportunities_and_without_work_json_file(year)
    with open(file_asks, "r") as file:
        data_1 = loads(file.read())

    if not isfile(file_offer):
        from data_analyze.ex import generate_opportunities_and_without_work_json_file
        generate_opportunities_and_without_work_json_file(year)
    with open(file_offer, "r") as file:
        data_2 = loads(file.read())

    data_1 = unsetBrackets(data_1[section])
    data_2 = unsetBrackets(data_2[section])

    null_elements1 = set(data_1.keys()) - set(data_2.keys())
    null_elements2 = set(data_2.keys()) - set(data_1.keys())

    for nul_el in list(null_elements1) + list(null_elements2):
        data_1[nul_el] = data_1.get(nul_el, 0)
        data_2[nul_el] = data_2.get(nul_el, 0)

    # both = set(list(data_1.keys()) + list(data_2.keys())) - null_elements1 - null_elements2

    return data_1, data_2  # data_1{квалификация: количество}


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
