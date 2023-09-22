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

    def verify_one(self,s,ip,port): # Verifica se uma porta está em uso
        
        try:
            if s.connect((ip,port)):
                print(f"socket pluged on {port}")
                s.close()
                return True
            else:
                print(f"A porta {port} está em uso")
                s.close()
                return False
            
        except Exception as e:
            print(f"A porta {port} está em uso, há uma aplicação rodando...")
            s.close()
            return False

    def verify_many(self,s,ip,ports): # Verifica estado das portas de aplicação
        log ={

        }
            
        for i in ports:
            a=self.verify_one(s,ip,i)
            log[i] = a

        return log

        
        
        
