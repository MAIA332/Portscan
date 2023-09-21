import socket

class scan:

    def __init__(self) -> None:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.hostname = socket.gethostname()
        self.ip_host = socket.gethostbyname(self.hostname)

    def listen_specify(self, s,ip,port):

        while True:
            if s.connect_ex((ip,port)):
                pass
            else:
                #data = s.recv(1024)
                #print(data.decode('ascii'))
                print('Porta abriu')
                s.close()
                break


    def verify(self,s,ip,ports):
        log ={

        }
            
        for i in ports:
            s.settimeout(1.0)
            res = s.connect_ex((ip,i))

            if res == 0:
                log[i]=True
                print(f'Porta {i} do host {ip} está aberta')

            else:
                log[i]=False
                print(f'Porta {i} do host {ip} está fechada')

        return log

        
        
        
