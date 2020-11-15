from bottle import route, run, error, template, request, response, Bottle
from json import dumps
app = application = Bottle()



# class EnableCors(object):
#     name = 'enable_cors'
#     api = 2
#
#     def apply(self, fn, context):
#         def _enable_cors(*args, **kwargs):
#             # set CORS headers
#             response.headers['Access-Control-Allow-Origin'] = '*'
#             response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
#             response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
#
#             if request.method != 'OPTIONS':
#                 # actual request; reply with the actual response
#                 return fn(*args, **kwargs)
#
#         return _enable_cors


def temp(file_name, *args,  title="", extension=".html", template_dir="view/", **kwargs):
    file_name = template_dir + file_name + extension
    return template("view/layout/skeleton.html", body_file=file_name)


if __name__ == '__main__':
    pass