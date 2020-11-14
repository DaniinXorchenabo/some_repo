if __name__ == '__main__':
    from os import getcwd
    from os.path import split as os_split

    path = os_split(getcwd())
    path = os_split(path[0])[0] if not bool(path[-1]) else path[0]
    print(path)
    from libs import *


def split_url_params(params: dict) -> dict:
    from functools import reduce


    renaming_dict = { "field_of_activity": "field_of_activity",
                      "qualification": "qualification",
                      "age": "age",
                      "work_years": "work_years",
                      "gender": "gender",
                      "спрос": "",
                      "предложение": ""
    }
    if_filter_range_year = lambda string: (f"({string.split('-')[0]} <= i < {string.split('-')[-1]})" if "-" in string else int(string))
    all_if_for_year = lambda arr: ("lambda i:" + " or ".join([i for i in arr if type(i) == str] + ["(i in [ " + reduce(lambda on, tw: f"{on}, {tw}", filter(lambda i: type(i) != str, arr)) + " ])"]))

    transform_val_dict = {"age": lambda arr: all_if_for_year(if_filter_range_year(arr)),
                          "work_years": lambda arr: all_if_for_year(if_filter_range_year(arr)),
                          "gender": lambda i: lambda param: param in {"m": ["м"], "w": ["ж"], "mw": ["м", "ж"]}.get(i, ["м", "ж"])}
    params = {renaming_dict.get(key, key): val.split("@") for key, val in params.items()}
    #
    return dict()



