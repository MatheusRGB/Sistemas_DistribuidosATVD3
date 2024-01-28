from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler 
from datetime import datetime

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('10.0.2.15',21212),requestHandler = RequestHandler) as server:
    server.register_introspection_functions()    

    mensagens = []

    def ip_return():
        return "10.0.84.181"

    def time_return():
        tempo = datetime.now()
        formato = "%m/%d/%Y, %H:%M:%S"
        return tempo.strftime(formato)
    
    def adicionar_mensagem(texto):
        mensagens.append(texto)
        
    def listar_mensagens():
        return mensagens
        

    server.register_function(ip_return, 'ip_return')
    server.register_function(time_return, 'data_hora')
    server.register_function(adicionar_mensagem, 'adicionar_mensagem')
    server.register_function(listar_mensagens, 'listar_mensagens')
    

