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


def job_and_workless(years: list, section: str, qualifications: set):
    job, workless = job_and_workless_base(years, qualifications)
    job = {years[ind]: val for ind, val in
           enumerate(map(lambda i: list(filter(lambda j: j[0] in qualifications, i.items())), job))}
    workless = {years[ind]: val for ind, val in enumerate(map(lambda i:
                                                              list(filter(lambda j: j[0] in qualifications, i.items())),
                                                              workless))}
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
        "(i in [ " + reduce(lambda on, tw: f"{on}, {tw}", filter(lambda i: type(i) != str, arr)) + " ])"]))
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


# job_and_workless([2017, 2018], ["Арматурщик", "Бетонщик", "Бухгалтер"])
# split_url_params(dict())
