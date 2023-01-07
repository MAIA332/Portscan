import socket

class scan:

    def listen_specify(self, s):
        ip = input('IPV4: ')
        port = int(input('PORT: '))

        while True:
            if s.connect_ex((ip,port)):
                pass
            else:
                #data = s.recv(1024)
                #print(data.decode('ascii'))
                print('Porta abriu')
                s.close()
                break


    def verify(self,s):
        ip = input('IPV4: ')
        ports = []

        
        while True:
            try:
                port = int(input('PORT: '))

                if port == 0000:
                    break

                ports.append(port)
                
                if(len(ports) == 10):
                    print('Limite de portas atingido')
                    break
            except:
                break
            
        for i in ports:
            s.settimeout(1.0)
            res = s.connect_ex((ip,i))

            if res == 0:
                print(f'Porta {i} do host {ip} está aberta')

            else:
                print(f'Porta {i} do host {ip} está fechada')
    



    def Main(self,):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        print("========================================")
        print("========================================")
        print("=== |Escutar Portas especificas (1)| ===\n=== |Verificar portas abertas (2)| ===")

            
        func = int(input('Scan-: '))

        if func == 1:
            self.listen_specify(s)

        elif func == 2:
            self.verify(s)
