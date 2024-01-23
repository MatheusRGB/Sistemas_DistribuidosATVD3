import xmlrpc.client

server = xmlrpc.client.ServerProxy('http://10.0.84.181:21212')

print("1 - Ip do Servidor\n")
print("2 - Data e Hora Atual\n")
print("3 - Armazenar Mensagem\n")
print("4 - Listar Mensagens")
op = input("Digite o numero da função que queira acessar\n")

if(op == 1):
    print(server.ip_return())

if(op == 2):
    print(server.data_hora())

print(server.data_hora())

