from data_analyze.asks_offer_changes import globalGetChanges
from json import loads
from data_analyze.countpeople import count_male
from data_analyze.countworkers import count_workers
from data_analyze.show import show


def getSpeedChange(close, n=1):
    changes = [close[i] - close[i - 1] for i in range(1, len(close))]
    return changes if n == 1 else getSpeedChange(changes, n - 1)


def predictArr(arr):
    df = sum(getSpeedChange(arr)) / (len(arr) - 1)
    return arr[-1] + df


def analyzeJob(job, data):
    array = [el[job] for el in data]
    return array


def analyzeJobs(data):
    arrs = {}
    for el in data:
        for job in el:
            arrs[job] = arrs.get(job, []) + [el[job]]

    return arrs


def analyzeSection(data):
    sec_ww = [sum(list(data[0].values())) / len(list(data[0].values()))]
    sec_op = [sum(list(data[1].values())) / len(list(data[1].values()))]
    print("Суммарно вакансии", sec_op)
    print("Суммарно спрос", sec_ww)


def analyze_workers():
    years, sectionsworkers = count_workers()
    for arr in sectionsworkers:
        print(arr)
        show([sectionsworkers[arr]], title=arr, namefile="plots/" + arr.replace(" ", "_").replace(":", "") + ".png")


def analyze_age():
    data = count_male()
    for male in ["male", "female"]:
        for age in data["male"]:
            arr = data["male"][age]
            print(arr)
            show([arr], title=f"{age}_{male}", namefile="plots/male/" + f"{age}_{male}")


without_work = []
opportunities = []

for year in [2017, 2018, 2019]:
    res = globalGetChanges(year, "РАЗДЕЛ F СТРОИТЕЛЬСТВО")
    without_work.append(res[0])
    opportunities.append(res[1])
    analyzeSection(res)

print(analyzeJobs(opportunities))
print(analyzeJobs(without_work))

analyze_workers()

analyze_age()
