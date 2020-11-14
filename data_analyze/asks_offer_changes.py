from json import loads, dumps

def unsetBrackets(anydict):
    arrkeys = list(map(lambda x: x[:x.find("(") - 1], list(anydict.keys())))
    arr_values = list(anydict.values())
    temp = [(arrkeys[i], arr_values[i]) for i in range(len(arr_values))]
    return dict(temp)


def globalGetChanges(file_asks, file_offer):
    with open(file_asks, "r") as file:
        data_1 = loads(file.read())

    with open(file_offer, "r") as file:
        data_2 = loads(file.read())

    section = 'РАЗДЕЛ F СТРОИТЕЛЬСТВО'

    data_1 = unsetBrackets(data_1[section])
    data_2 = unsetBrackets(data_2[section])

    null_elements1 = set(data_1.keys()) - set(data_2.keys())
    null_elements2 = set(data_2.keys()) - set(data_1.keys())

    both = set(list(data_1.keys()) + list(data_2.keys())) - null_elements1 - null_elements2

    return both, data_1, data_2  # data_1{квалификация: количество}


globalGetChanges("/content/without_work2019.json", "opportunities2019.json")
