import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='sistema_hamburgeria'
)
cursor = conexao.cursor()

id = 1
nome = "Clássico"
valor = 19.99

#Inserir Valores
#comando = f'INSERT INTO hamburgeres (id_hamb, nome_hamb, preco_hamb) VALUES ({id}, "{nome}", {valor})' #Comando a ser executado
#cursor.execute(comando) #Execução do comando
#conexao.commit() #Commit/envio do comando para a database
#-------------------------------------------------------------------------

#Ler valores
#comando = f'SELECT preco_hamb FROM hamburgeres WHERE id_hamb = 1;'  # Comando a ser executado
#cursor.execute(comando)  # Execução do comando
#resultado = cursor.fetchall() #Le os dados que foram requisitados
#valor_tratado = float(resultado[0][0]) #Trata o valor da variavel "Resultado"
#print(valor_tratado)#Exibe o valor da variavel

#--------------------------------------------------------------------------

#Editar Valores
#comando = f'UPDATE hamburgeres SET preco_hamb = {valor} WHERE id_hamb = {id}' #Comando a ser executado
#cursor.execute(comando) #Execução do comando
#conexao.commit() #Commit/envio do comando para a database
#--------------------------------------------------------------------------

#Deletar Valores
#comando = f'DELETE FROM hamburgeres WHERE id_hamb = {id}' #Comando a ser executado
#cursor.execute(comando) #Execução do comando
#conexao.commit() #Commit/envio do comando para a database
#-------------------------------------------------------------------------

cursor.close()
conexao.close()