import os

def home(environ, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    responsestring = "Hello Mouli's World for " + environ['PATH_INFO']
    return responsestring

def login(environ, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return "This is the Login page..."

def logout(environ, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return "This is the Logout page..."

def getenv(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)

    html = "<html><body><ol>"
    for i, j in os.environ.items():
        #print(i, j)
        html+= "<li>{} : {}</li>".format(i, j)

    html += "</ol></body></html>"
    return html.encode("utf-8")



def application(environ, start_response):
    if '/home' == environ['PATH_INFO']:
        return home(environ, start_response);
    elif '/login' == environ['PATH_INFO']:
        return login(environ, start_response);
    elif '/logout' == environ['PATH_INFO']:
        return logout(environ, start_response);
    elif '/getenv' == environ['PATH_INFO']:
        return getenv(environ, start_response);
    else:
        start_response('200 OK', [('Content-Type','text/html')])
        # readbytes = environ['PATH_INFO'].read() # returns bytes object
        # readstr = readbytes.decode('utf-8')      # returns str object
        responsestring = "Hello Mouli's World for " + environ['PATH_INFO']
        # return [b"Hello Mouli's World"]
        return responsestring
    