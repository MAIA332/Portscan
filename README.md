# Estudo de Segurança com Python e Socket

Bem-vindo ao repositório de Estudo de Segurança com Python e Socket! Este projeto foi criado com o objetivo de explorar conceitos de segurança cibernética através da programação em Python, usando a biblioteca `socket` para a criação de um script que escuta portas em um computador. O intuito principal é entender as vulnerabilidades potenciais e como implementar medidas preventivas.

## Objetivo

O foco deste repositório é oferecer um espaço para aprendizado e prática de segurança cibernética, demonstrando como a biblioteca `socket` pode ser usada para escutar portas e identificar possíveis vulnerabilidades em um sistema. O script não tem qualquer intenção maliciosa e é destinado a fins educacionais.

## Recursos e Destaques

- Utilização da biblioteca `socket` do Python para a criação do script.
- Escuta de Portas: O script permite escutar portas específicas no computador.
- Detecção de Conexões: Mostra informações sobre conexões estabelecidas.
- Foco na Prevenção: O projeto busca explorar vulnerabilidades para ilustrar a importância de medidas preventivas.

## Como Usar

1. Clone ou faça o download do repositório para sua máquina local.
2. Abra o arquivo `_scn_.py` em um ambiente Python.
3. Edite as configurações para escolher a porta que deseja escutar.
4. Execute o script e observe as informações de conexão.
5. Explore o código-fonte para entender como a biblioteca `socket` é aplicada.

### Exemplo de código:

```
from Portscan._scn_ import scan

port_mapping ={
    "MySQL":3306,
    "HTTP":80
}

for i in port_mapping:  
    a= scan()  
    is_used = "ONLINE" if a.verify_one(a.s,"localhost",port_mapping[i]) == True else "OFFLINE"
    PID = a.get_pid_using_port(port_mapping[i])
    print(f"{i} port: {is_used} ; PID: {PID}")
```

**Output:**

```
MySQL port: OFFLINE ; PID: None
HTTP port: OFFLINE ; PID: None
```

**Ou**
```
MySQL port: ONLINE ; PID: 23148
HTTP port: ONLINE ; PID: 19132
```

## Aviso Importante

Este repositório é destinado apenas a fins educacionais. É fundamental utilizar o conhecimento adquirido de forma ética e responsável. Não é recomendado realizar testes em sistemas sem a devida autorização.

Este projeto é uma oportunidade valiosa para aprender sobre segurança cibernética, explorando a biblioteca `socket` do Python e compreendendo como a detecção de portas pode ajudar a identificar vulnerabilidades em sistemas.

---

<p align="center">
  Feito com ❤️ por Lukas Maia
</p>
