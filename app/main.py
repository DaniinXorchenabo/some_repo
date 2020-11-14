from funcs.libs import *
from funcs.funcs import *


@route('/hello')
def hello():
    return "Hello World!"


@route('/test', method=["GET", "POST"])
def root_thie_site():
    #  <url>?field_of_activity=bool_or_name&qualification=bool_or_name&age=1@3@5-10&work_years=1@3@5-10&gender=m|w|mw
    print('test')

    if request.GET:
        params = split_url_params(dict(request.params))
        print(params)
        rv = [{"id": 1, "name": "Test Item 1"}, {"id": 2, "name": "Test Item 2"}]
        response.content_type = 'application/json'
        print(dumps(rv))
        return dumps(rv)
    # http://localhost:8080/test?is_work=yes
    # return template('Здравствуй {{name}}, как дела?', name="Dfcz")
    return temp("main_page", param="dfdf")


@route('/')
def root_thie_site():
    # return template('Здравствуй {{name}}, как дела?', name="Dfcz")
    return temp("main_page", param="dfdf")


@error(404)
def error404(error):
    return 'Упс, извините страница не найдена!\n'


if __name__ == '__main__':
    from functools import reduce
    print()

    if_filter_range_year = lambda string: (f"({string.split('-')[0]} <= i < {string.split('-')[-1]})" if "-" in string else int(string))
    all_if_for_year = lambda arr: eval("lambda i:" + " or ".join([i for i in arr if type(i) == str] + ["(i in [ " + reduce(lambda on, tw: f"{on}, {tw}", filter(lambda i: type(i) != str, arr)) + " ])"]))
    string = "1@2@3@4@5@8-10@14-20"
    string = [if_filter_range_year(i) for i in string.split("@")]
    print(all_if_for_year(string))
    run(host='localhost', port=8080, debug=True)
