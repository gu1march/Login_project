import cx_Oracle

# Informações de conexão
username = 'seu_usuario'
password = 'sua_senha'
host = 'localhost'  # Endereço do servidor
port = 1521        # Número da porta padrão do Oracle
service_name = 'seu_service_name'  # Ou substitua por SID, caso esteja usando

# String de conexão
dsn = cx_Oracle.makedsn(host, port, service_name=service_name)

# Conectar ao banco de dados
connection = cx_Oracle.connect(username, password, dsn)