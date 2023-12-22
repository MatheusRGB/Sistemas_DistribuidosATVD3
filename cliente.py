import socket
import threading

def receber_mensagens(sock):
    while (True):
        data = sock.recv(2048)
        mensagem = data.decode()
        if mensagem!='-1':
            #Imprimindo a mensagem recebida
            print(data.decode())
            break
            


sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    
server_address = ('localhost', 20001)
print ("Conectando %s porta %s" % server_address)
#Conectando ao servidor

recepcao = threading.Thread(target=receber_mensagens,args=(sock,))
recepcao.start()
while (True):
    comando = input("Digite 1 para acessar as funções do servidor:\n")
    if(comando == '1'):
        message = input("Digite a mensagem a ser enviada: \n")
        #Enviando mensagem ao servidor
        sock.sendto(message.encode('utf-8'),server_address)
        break
    

recepcao.join()