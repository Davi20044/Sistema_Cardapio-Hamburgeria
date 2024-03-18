import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='sistema_hamburgeria'
)
cursor = conexao.cursor()

#Inserir Valores
id = 1
nome = "Clássico"
valor = 19.99

comando = f'INSERT INTO hamburgeres (id_hamb, nome_hamb, preco_hamb) VALUES ({id}, "{nome}", {valor})' #Comando a ser executado
cursor.execute(comando) #Execução do comando
conexao.commit() #Commit/envio do comando para a database
#-------------------------------------------------------------------------

#Inserir Valores
id = 2
nome = "Salad"
valor = 24.99

comando = f'INSERT INTO hamburgeres (id_hamb, nome_hamb, preco_hamb) VALUES ({id}, "{nome}", {valor})' #Comando a ser executado
cursor.execute(comando) #Execução do comando
conexao.commit() #Commit/envio do comando para a database
#-------------------------------------------------------------------------

#Inserir Valores
id = 3
nome = "Bacon"
valor = 29.99

comando = f'INSERT INTO hamburgeres (id_hamb, nome_hamb, preco_hamb) VALUES ({id}, "{nome}", {valor})' #Comando a ser executado
cursor.execute(comando) #Execução do comando
conexao.commit() #Commit/envio do comando para a database
#-------------------------------------------------------------------------

#Inserir Valores
id = 4
nome = "Double"
valor = 39.99

comando = f'INSERT INTO hamburgeres (id_hamb, nome_hamb, preco_hamb) VALUES ({id}, "{nome}", {valor})' #Comando a ser executado
cursor.execute(comando) #Execução do comando
conexao.commit() #Commit/envio do comando para a database
#-------------------------------------------------------------------------

#Inserir Valores
id = 5
nome = "Especial"
valor = 49.99

comando = f'INSERT INTO hamburgeres (id_hamb, nome_hamb, preco_hamb) VALUES ({id}, "{nome}", {valor})' #Comando a ser executado
cursor.execute(comando) #Execução do comando
conexao.commit() #Commit/envio do comando para a database
#-------------------------------------------------------------------------

#Ler valores
comando = f'SELECT * FROM hamburgeres'  # Comando a ser executado
cursor.execute(comando)  # Execução do comando
resultado = cursor.fetchall() #Le os dados que foram requisitados
print(resultado)

#--------------------------------------------------------------------------



cursor.close()
conexao.close()