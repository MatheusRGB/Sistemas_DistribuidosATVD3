import socket
import threading
from datetime import datetime
conta = 0

def conexao_cliente(client,address):
    global conta
    while (True):    
        '''
        PROTOCOLO
        '''
        mensagem = client.decode()

        if(mensagem == 'chamadas'):
            sock.sendto(f'{conta}'.encode(), address)
            break


        if (mensagem=='hora'):
            
            conta = conta + 1
            sock.sendto(f'{datetime.now()}'.encode(), address)
            break

        client.close()
        
    
    #Fechando o socket
    

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    
server_address = ('localhost', 20001)
print ("Iniciando servidor na porta %s %s" % server_address)
#Reservando porta
sock.bind(server_address)

while True:
    client = sock.recvfrom(2048)
    conexao = threading.Thread(target=conexao_cliente,args=(client[0],client[1]))
    conexao.start()

