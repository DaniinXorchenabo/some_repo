# -*- coding: utf-8 -*-
from funcs.libs import *
from funcs.funcs import *
from bottle import route, run, error, template, request, response, Bottle
from db.models import *
from pony.orm import *


@app.route('/test', method=["GET", "POST"])  #
def root_thie_site():
    response.set_header('Access-Control-Allow-Origin', '*')
    response.add_header('Access-Control-Allow-Methods', 'GET, POST, PUT, OPTIONS')
    # response.headers['Content-type'] = 'application/json'
    #  <url>?field_of_activity=bool_or_name&qualification=bool_or_name&age=1@3@5-10&work_years=1@3@5-10&gender=m|w|mw
    # ?field_of_activity=РАЗДЕЛ F СТРОИТЕЛЬСТВО&qualification=Бетонщик&year=2017-2019&job_opening&proposal_workless
    print('test')

    if request.GET:
        # .decode('utf8')
        data = split_url_params_2(dict(request.params.decode()))
        response.content_type = 'application/json'
        return dumps(data)
    # http://localhost:8080/test?is_work=yes
    # return template('Здравствуй {{name}}, как дела?', name="Dfcz")
    return "amother_some_page"  #  temp("main_page", param="dfdf")


@app.route('/get_section', method=["GET", "POST"])  # - список сфер
def get_section():
    from data_analyze.asks_offer_changes import get_all_section
    # print(*get_all_section(), sep='\n')
    return dumps(get_all_section())


@app.route('/get_qualification', method=["GET", "POST"])  # ?section=сфера - список квалификаций
def get_qualification():
    if request.GET:
        from data_analyze.asks_offer_changes import get_qualifications_from_section

        section = [i for i in dict(request.params.decode()).values()][0]
        data = get_qualifications_from_section(section)
        return dumps(data)
    return "some page...."


@app.route('/get_years', method=["GET", "POST"])  # ?section_flag - список годов
def get_years():
    from data_analyze.asks_offer_changes import get_years

    return dumps(get_years())


@app.route('/')
def root_thie_site():
    # return template('Здравствуй {{name}}, как дела?', name="Dfcz")
    return "main page 1111"

@app.route('/registration', method=["GET", "POST"])  # ?name=you_login&password=you_password&email=you_emmeil
@db_session
def registration():
    if request.GET:
        data = dict(request.params.decode())
        messeng = [(User.exists(name=data.get('name', '')), "Пользователь с таким именем уже существует!"),
                   (User.exists(email=data.get('email', '')), "Пользователь с таким emeil уже существует!")]
        messeng = [i[1] for i in messeng if i[0]]
        if not bool(messeng):
            messeng = "ok"
            try:
                User(**data)
                commit()
            except Exception as e:
                messeng = "На сервере произошла какая-то неизвестеая ошибка, к сожалению, не удалось вас зарегестрировать как пользователя"
                print("произошла неизвестная ошибка в @app.route('/registration':", e )
        print(messeng)
        return dumps({"messeng": messeng})
    return "some_page"

@app.route('/login', method=["GET", "POST"])  # ?name=you_login&password=you_password
@db_session
def registration():
    if request.GET:
        try:
            data = dict(request.params.decode())
            messeng = "Вы успешно авторизованы!"
            if not User.exists(name=data.get('name', '')):
                messeng = "В нашей базе банный нет пользователя с таким именем...("
            else:
                user = User.get(name=data.get('name', ''))
                if user.password != data.get('password', ''):
                    messeng = "Неверно ввелён пароль"
        except Exception as e:
            messeng = "На сервере произошла какая-то неизвестеая ошибка, к сожалению, вам не удалось авторизоваться как пользователю("
            print("произошла неизвестная ошибка в @app.route('/login':", e)
        print(messeng)
        return dumps({"messeng": messeng})
    return "some_page"

if __name__ == '__main__':
    # app.install(EnableCors())
    run(app=app, host="0.0.0.0", port=8090, quiet=False, reloader=False)
