import xmlrpc.client
from datetime import datetime

server = xmlrpc.client.ServerProxy('http://10.0.2.15:21212')

print("1 - Ip do Servidor\n")
print("2 - Data e Hora Atual\n")
print("3 - Armazenar Mensagem\n")
print("4 - Listar Mensagens")
op = input("Digite o numero da função que queira acessar\n")
mensagens = []
def escolha(op):
    if(op == '1'):
        ip = server.ip_return()
        print(ip)

    if(op == '2'):
        data = server.data_hora()
        print(data)

    if(op == '3'):
        texto = input("Digite sua mensagem\n")
        server.adicionar_mensagem(texto)
        print("Mensagem adicionada")    

    if(op == '4'):
        mensagens = server.listar_mensagens()
        print("Mensagens disponiveis:\n")
        for mensagem in mensagens:
            print(mensagem)



