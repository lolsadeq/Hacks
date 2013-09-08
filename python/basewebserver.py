import BaseHTTPServer

class WebRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/foo':
            self.send_response(200)
            self.do_something()
        else: 
            self.send_error(404)
            
    def do_something(self):
        print 'hello world'
        
server = BaseHTTPServer.HTTPServer(('127.0.0.1',80), WebRequestHandler)
server.serve_forever()

