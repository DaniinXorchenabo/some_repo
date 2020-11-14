from json import loads, dumps
from os.path import isfile

def unsetBrackets(anydict):
    arrkeys = list(map(lambda x: x[:x.find("(") - 1], list(anydict.keys())))
    arr_values = list(anydict.values())
    temp = [(arrkeys[i], arr_values[i]) for i in range(len(arr_values))]
    return dict(temp)


def globalGetChanges(year, section):
    file_asks = str(f"output/without_work{year}.json")
    file_offer = str(f"output/opportunities{year}.json")
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


if __name__ == '__main__':
    a = globalGetChanges(2018, section="РАЗДЕЛ F СТРОИТЕЛЬСТВО")
    print(a)