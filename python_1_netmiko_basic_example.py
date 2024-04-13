# Importa a classe ConnectHandler da biblioteca netmiko
from netmiko import ConnectHandler

# Cria um dicionário com as configurações necessárias para a conexão
cisco_device = {
    'device_type': 'cisco_xe',  # Define o tipo do dispositivo, neste caso um Cisco IOS XE
    'host':   '10.0.254.1',     # Endereço IP do dispositivo ao qual vamos nos conectar
    'username': 'netautomation',# Nome de usuário para a autenticação
    'password': 'Admin@123',    # Senha para a autenticação
    'port' : 22,                # Porta para a conexão SSH, 22 é o padrão
}

# Utiliza o dicionário de configuração para criar uma conexão SSH com o dispositivo
net_connect = ConnectHandler(**cisco_device)

# Envia um comando para o dispositivo e armazena a saída em uma variável
output = net_connect.send_command('show ip int brief')

# Exibe a saída do comando
print(output)

