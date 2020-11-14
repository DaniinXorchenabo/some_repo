# -*- coding: utf-8 -*-
from funcs.libs import *
from funcs.funcs import *


@app.route('/hello')
def hello():
    return "Hello World!"


@app.route('/test', method=["GET", "POST"])
def root_thie_site():
    #  <url>?field_of_activity=bool_or_name&qualification=bool_or_name&age=1@3@5-10&work_years=1@3@5-10&gender=m|w|mw
    # ?field_of_activity=РАЗДЕЛ F СТРОИТЕЛЬСТВО&qualification=Бетонщик&year=2017-2019&job_opening&proposal_workless
    print('test')

    if request.GET:
        #.decode('utf8')
        params = split_url_params_2({key.decode('utf8'): val.decode('utf8') for key, val in dict(request.params).items()})
        # print(params)
        rv = [{"id": 1, "name": "Test Item 1"}, {"id": 2, "name": "Test Item 2"}]
        response.content_type = 'application/json'
        # print(dumps(rv))
        return dumps(rv)
    # http://localhost:8080/test?is_work=yes
    # return template('Здравствуй {{name}}, как дела?', name="Dfcz")
    return temp("main_page", param="dfdf")


@app.route('/')
def root_thie_site():
    # return template('Здравствуй {{name}}, как дела?', name="Dfcz")
    return "main page 1111"



if __name__ == '__main__':
    app.install(EnableCors())
    run(app=app, host="0.0.0.0", port=8090, quiet=False, reloader=False)
