from bottle import route, run, error, template, request, response
from json import dumps


def temp(file_name, *args,  title="", extension=".html", template_dir="view/", **kwargs):
    file_name = template_dir + file_name + extension
    return template("view/layout/skeleton.html", body_file=file_name)


if __name__ == '__main__':
    pass