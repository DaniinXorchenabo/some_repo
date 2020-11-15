if __name__ == '__main__':
    from os import getcwd
    from os.path import split as os_split

    path = os_split(getcwd())
    path = os_split(path[0])[0] if not bool(path[-1]) else path[0]
    print(path)
    from libs import *


def job_and_workless_base(years: list, section: str, qualifications: set):
    from data_analyze.asks_offer_changes import globalGetChanges

    job, workless = zip(*[globalGetChanges(year, section) for year in years])
    return job, workless


def job_only(years: list, section: str, qualifications: set):
    job, _ = job_and_workless_base(years, qualifications)
    job = {years[ind]: val for ind, val in
           enumerate(map(lambda i: list(filter(lambda j: j[0] in qualifications, i.items())), job))}
    return job


def workless_only(years: list, section: str, qualifications: set):
    _, workless = job_and_workless_base(years, qualifications)
    workless = {years[ind]: val for ind, val in enumerate(map(lambda i:
                                                              list(filter(lambda j: j[0] in qualifications, i.items())),
                                                              workless))}
    return workless


def job_and_workless(years: list , section: str, qualifications: set):
    job, workless = job_and_workless_base(years, qualifications)
    job =       {years[ind]: val for ind, val in enumerate(map(lambda i: list(filter(lambda j: j[0] in qualifications, i.items())), job))}
    workless =  {years[ind]: val for ind, val in enumerate(map(lambda i: list(filter(lambda j: j[0] in qualifications, i.items())), workless))}
    return job, workless

    # print(*job.items(), sep="\n", end="\n--------------\n")
    # print(*workless.items(), sep="\n", end="\n--------------\n")


def job_and_workless_count_filt(data_func):
    return lambda years, section, qualifications, row_nums: list(
        filter(create_filt_from_number_set(row_nums), data_func(years, section, qualifications)))


def create_filt_from_number_set(arr):
    from functools import reduce

    if_filter_range_year = lambda string: (
        f"({string.split('-')[0]} <= i < {string.split('-')[-1]})" if "-" in string else int(string))
    all_if_for_year = lambda arr: ("lambda i:" + " or ".join([i for i in arr if type(i) == str] + [
        "(i in [ " + reduce(lambda on, tw: f"{on}, {tw}", list(filter(lambda i: type(i) != str, arr)) + ['-1 ', '-1 ']) + " ])"]))
    return eval(all_if_for_year([if_filter_range_year(i) for i in arr.split('@')]))


def split_url_params(params: dict) -> dict:
    if "field_of_activity" not in params or "qualification" not in params:
        return dict()
    set_keys = set(params.keys()) - {"field_of_activity", "qualification"}
    data_sets = {
        frozenset(("year", "job_opening", "proposal_workless")): job_and_workless,
        frozenset(("year", "job_opening", "proposal_workless", "count_filt")): job_and_workless_count_filt(
            job_and_workless),
        frozenset(("year", "job_opening")): job_only,
        frozenset(("year", "proposal_workless")): workless_only,
    }
    if set_keys in data_sets:
        data_sets[frozenset(set_keys)]()

    renaming_dict = {"field_of_activity": "field_of_activity",
                     "qualification": "qualification",
                     "age": "age",
                     "work_years": "work_years",
                     "gender": "gender",
                     "job_opening": "job_opening",
                     "proposal_workless": "proposal_workless",
                     "year": "year",
                     "count_filt": "count_filt"
                     }

    transform_val_dict = {"age": create_filt_from_number_set,
                          "work_years": create_filt_from_number_set,
                          "gender": lambda i: lambda param: param in {"m": ["м"], "w": ["ж"], "mw": ["м", "ж"]}.get(i, [
                              "м", "ж"])}

    params = {renaming_dict.get(key, key): transform_val_dict.get(key, lambda i: i)(val) for key, val in params.items()}
    print(params)
    return dict()


#----------------------------------------------
def split_url_params_2(params: dict):
    # print('--=-=-=', params)
    if "field_of_activity" not in params or "qualification" not in params:
        return dict()
    field = params.pop("field_of_activity")
    qualif = set(params.pop("qualification").split('@'))
    job_opening = params.pop("job_opening", None)
    proposal_workless = params.pop("proposal_workless", None)
    params = create_filt_from_param(params)
    # print(type(params), params['unreal_key'])

    data = get_data(field=field, qualif=qualif, job_opening=job_opening, proposal_workless=proposal_workless, filt=params)
    data = decorate_data(data)
    return data

def create_filt_from_param(param: dict):
    from datetime import date
    from collections import defaultdict

    # print(param)
    transforming_dict = {
        "age": create_filt_from_number_set,
        "work_years": create_filt_from_number_set,
        "year": create_filt_from_number_set,
        "count_filt": create_filt_from_number_set,
        "gender": lambda i: lambda param: param in {"m": ["м"], "w": ["ж"], "mw": ["м", "ж"]}.get(i, ["м", "ж"])
    }
    defoult_filt_dict = {"year": lambda i: i == date.today().year}
    param = {key: transforming_dict[key](val) for key, val in param.items()}
    # print(param)
    defoult_filt_dict.update(param)
    param1 = defaultdict(lambda: lambda *a, **k: True)
    param1.update(defoult_filt_dict)
    # print(param)
    return param1

def get_work_and_job_data(field, filt=lambda *a, **k: True, **kwargs):
    from data_analyze.asks_offer_changes import globalGetChanges

    return zip(*[globalGetChanges(year, field, **kwargs) for year in filter(filt, range(1900, 2100))])

def get_data(field=None, qualif=set(), filt=dict(), **kwargs):
    if field:
        # print(filt.get("unreal_key"))
        data = get_work_and_job_data(field, filt.pop("year", lambda *a, **k: True), **kwargs)
        data = [map(lambda i: list(filter(lambda j: j[0] in qualif, i.items())), dat) for dat in data]
        # print(filt.get("count_filt1"), filt.get("unreal_key"))
        data = [list(map(lambda i: list(filter(lambda j: filt.get("count_filt", lambda *a, **k: True)(j[1]), i)), dat)) for dat in data]
        print('--&&^^^^^', *[list(i) for i in data], sep='\n')
        # data = [[one_year for one_year in dat] for dat in data]
        return data

def decorate_data(data):

    return data