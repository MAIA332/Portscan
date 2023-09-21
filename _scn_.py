class scan:

    def __init__(self) -> None:
        import socket
        import os

        self.os = os
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.hostname = socket.gethostname()
        self.ip_host = socket.gethostbyname(self.hostname)

    def listen_specify(self, s,ip,port):

        while True: # Escuta uma porta até que ela abra
            if s.connect_ex((ip,port)):
                pass
            else:
                print('Porta abriu')
                s.close()
                break

    def plug(self,s,ip,port): # Verifica se uma porta está em uso
        
        try:
            if s.connect((ip,port)):
                print(f"socket pluged on {port}")
            else:
                print(f"A porta {port} está em uso")

        except Exception as e:
            print(f"A porta {port} está em uso {e}")


    def verify(self,s,ip,ports): # Verifica estado das portas de aplicação
        log ={

        }
            
        for i in ports:
            s.settimeout(1.0)
            res = s.connect_ex((ip,i))
            print(res)

            if res == 0:
                log[i]=True

            elif res == 10060  or res == 10051 or res == 111 or res == 10035:
                log[i]="Fechada"

            elif res == 10056:
                log[i] = "Não autorizada"

        return log

        
        
        
