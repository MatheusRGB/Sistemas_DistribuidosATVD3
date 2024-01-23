from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler 
from datetime import datetime

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('10.0.84.181',21212),requestHandler = RequestHandler) as server:
    server.register_introspection_functions()    

    def soma_function(x, y):
        return x + y

    def sub_function(x, y):
        return x - y

    def ip_return():
        ip = '10.0.84.181'
        return ip

    def time_return():
        tempo = datetime.strftime("%m/%d/%Y, %H:%M:%S")
        return 5
        

    server.register_function(soma_function, 'soma')
    server.register_function(ip_return, 'ip_return')
    server.register_function(time_return, 'data_hora')

    server.serve_forever()
    

