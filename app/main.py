from bottle import route, run, error, template
from decorate_standart.decorate_standart_func import *

@route('/hello')
def hello():
    return "Hello World!"


@route('/')
def root_thie_site():
    # return template('Здравствуй {{name}}, как дела?', name="Dfcz")
    return temp("main_page", param="dfdf")


@error(404)
def error404(error):
    return 'Упс, извините страница не найдена!\n' + str(error)


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)