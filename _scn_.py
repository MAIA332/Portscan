class scan:

    def __init__(self) -> None:
        self.socket = __import__("socket")
        self.os = __import__("os")
        self.psutil = __import__("psutil")

        self.s = self.socket.socket(self.socket.AF_INET, self.socket.SOCK_STREAM)
        self.hostname = self.socket.gethostname()
        self.ip_host = self.socket.gethostbyname(self.hostname)

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
            s.settimeout(1)
            # Tenta se conectar à porta, se ele conseguir se conectar na porta é por que alguma outra aplicação já a abriu
            s.connect((ip, port))
            s.close()
            return True
        except (self.socket.timeout, ConnectionRefusedError):
            return False


    def get_service_name(self,s,port):
        # Obtém o nome do serviço associado à porta
        try:
            service_name = self.socket.getservbyport(port)
            return service_name
        except OSError as e:
            return f"Serviço desconhecido: {e}"
        
    def get_pid_using_port(self,port):
        # Obtém o PID associado à porta
        for conn in self.psutil.net_connections():
            if conn.laddr.port == port:
                return conn.pid
        return None

    def terminate_process(self,pid):
        try:
            process = self.psutil.Process(pid)
            process.terminate()
            print(f"Processo com PID {pid} terminado com sucesso.")
        except self.psutil.NoSuchProcess:
            print(f"O processo com PID {pid} não foi encontrado.")
        except self.psutil.AccessDenied:
            print(f"Não foi possível encerrar o processo com PID {pid}. Permissão negada.")

            
        
        
