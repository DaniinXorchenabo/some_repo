from bottle import route, run, error, template

MY_TEMPLATE_PATH = "venw/"

def temp(file_name, *args,  title="", extension=".html", template_dir="view/", **kwargs):
    file_name = template_dir + file_name + extension
    return template("view/layout/skeleton.html", body_file=file_name)




if __name__ == '__main__':
    pass