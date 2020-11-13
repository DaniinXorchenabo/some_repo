from bottle import route, run, error, template


@route('/hello')
def hello():
    return "Hello World!"

@route('/')
def root_thie_site():
    return template("view/main_page.html")


@error(404)
def error404(error):
    return 'Упс, извините страница не найдена!\n' + str(error)

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)