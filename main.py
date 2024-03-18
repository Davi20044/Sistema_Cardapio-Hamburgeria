from tkinter import *  # Importa a biblioteca gráfica
import mysql.connector  # Importa a biblioteca MySQL

# Conexão com banco de dados
conexao = mysql.connector.connect(  # Seta a conexão com o banco de dados
    host='localhost',
    user='root',
    password='root',
    database='sistema_hamburgeria'
)
cursor = conexao.cursor()  # Seta o cursor
# --------------------------------------------------------------------------------------------------------

#-------------------------------Função centralizar janela
def centralizar_janela(janela):
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'+{x}+{y}')
#--------------------------------------------------------------------------------------------------------

#--------------------------------------Função exibir Vendas----------------------------------------------
def abrir_janela_venda():
    global janela_venda  # Definindo janela_venda como uma variável global

    # Esconder a janela inicial
    janela_init.withdraw()

    # Função para somar o valor do produto ao total
    def somar_valor(preco_produto):
        nonlocal valor_total
        valor_total += preco_produto
        label_valor_total.config(text=f"Valor Total: R$ {valor_total:.2f}")

    # Função para redefinir o valor total
    def reiniciar_valor():
        nonlocal valor_total
        valor_total = 0
        label_valor_total.config(text="Valor Total: R$ 0.00")

    # Função para processar o clique do botão
    def clique_produto(id_produto, nome_produto, preco_produto):
        somar_valor(preco_produto)

    # Consulta para obter os produtos da tabela 'hamburgeres'
    cursor.execute("SELECT id_hamb, nome_hamb, preco_hamb FROM hamburgeres")
    produtos = cursor.fetchall()

    # Janela de Venda
    janela_venda = Tk()
    janela_venda.title("Venda")

    # Criar botões para cada produto
    for id_produto, nome_produto, preco_produto in produtos:
        botao_produto = Button(janela_venda, text=nome_produto, command=lambda id_produto=id_produto, nome_produto=nome_produto, preco_produto=preco_produto: clique_produto(id_produto, nome_produto, preco_produto))
        botao_produto.pack(padx=5, pady=5)

    # Botão para reiniciar o valor total
    botao_reiniciar = Button(janela_venda, text="Reiniciar", command=reiniciar_valor)
    botao_reiniciar.pack(padx=5, pady=5)

    # Label para exibir o valor total
    valor_total = 0
    label_valor_total = Label(janela_venda, text=f"Valor Total: R$ {valor_total:.2f}")
    label_valor_total.pack()

    janela_venda.protocol("WM_DELETE_WINDOW", fechar_janela_venda)

    centralizar_janela(janela_venda)  # Centraliza a janela inicial

    janela_venda.mainloop()

def fechar_janela_venda():
    global janela_venda  # Definindo janela_venda como uma variável global

    janela_venda.destroy()
    janela_init.deiconify()

#--------------------------------------------------------------------------------------------------------

#------------------------------Função exibir Adição------------------------------------------------------
def abrir_janela_adicao():
    # Esconder a janela inicial
    janela_init.withdraw()

    def salvar():
        id_hamb = entrada_id.get()  # Obtém o valor do campo de ID
        nome_hamb = entrada_nome.get()  # Obtém o valor do campo de nome
        preco_hamb = entrada_preco.get()  # Obtém o valor do campo de preço

        comando = f'INSERT INTO hamburgeres (id_hamb, nome_hamb, preco_hamb) VALUES ({id_hamb}, "{nome_hamb}", {preco_hamb})'  # Comando a ser executado
        cursor.execute(comando)  # Execução do comando
        conexao.commit()  # Commit/envio do comando para a database

        # Fechar a janela de adição após salvar os dados
        janela_adit.destroy()
        janela_init.deiconify()  # Mostra a janela inicial quando a janela de adição for fechada

    # Janela de Adição
    janela_adit = Tk()  # Cria Janela
    janela_adit.title("Adicionar Item")  # Define o nome da Janela

    texto_inicial = Label(janela_adit, text="Adicione um item do cardapio", font=("Helvetica", 20), fg="red")  # Cria uma label de texto
    texto_inicial.pack(anchor="center", padx=10, pady=10)  # Define a posição da label

    # Campo de ID
    label_id = Label(janela_adit, text="ID:")
    label_id.pack()
    entrada_id = Entry(janela_adit)
    entrada_id.pack()

    # Campo de Nome
    label_nome = Label(janela_adit, text="Nome:")
    label_nome.pack()
    entrada_nome = Entry(janela_adit)
    entrada_nome.pack()

    # Campo de Preço
    label_preco = Label(janela_adit, text="Preço:")
    label_preco.pack()
    entrada_preco = Entry(janela_adit)
    entrada_preco.pack()

    botao_salvar = Button(janela_adit, text="Salvar", command=salvar)  # Cria um botão para salvar os dados
    botao_salvar.pack(anchor="center", padx=5, pady=5)  # Salva as informações dos campos de texto

    def fechar_janela_adicao():
        janela_adit.destroy()
        janela_init.deiconify()  # Mostra a janela inicial quando a janela de adição for fechada

    janela_adit.protocol("WM_DELETE_WINDOW", fechar_janela_adicao)  # Configura a ação ao fechar a janela

    centralizar_janela(janela_adit)  # Centraliza a janela inicial

    janela_adit.mainloop()  # Mantem a janela aberta, Último código da janela
#--------------------------------------------------------------------------------------------------------

#----------------------------------------Função exibir subtração-----------------------------------------
def abrir_janela_subtracao():
    # Esconder a janela inicial
    janela_init.withdraw()

    def excluir():
        id_hamb = entrada_id.get()  # Obtém o valor do campo de ID

        comando = f'DELETE FROM hamburgeres WHERE id_hamb = {id_hamb}'  # Comando a ser executado
        cursor.execute(comando)  # Execução do comando
        conexao.commit()  # Commit/envio do comando para a database

        # Fechar a janela de subtração após excluir os dados
        janela_sub.destroy()
        janela_init.deiconify()  # Mostra a janela inicial quando a janela de subtração for fechada

    # Janela de Subtração
    janela_sub = Tk()  # Cria Janela
    janela_sub.title("Excluir Item")  # Define o nome da Janela

    texto_inicial = Label(janela_sub, text="Retire um item do Cardapio", font=("Helvetica", 20), fg="red")  # Cria uma label de texto
    texto_inicial.pack(anchor="center", padx=10, pady=10)  # Define a posição da label

    # Campo de ID para excluir
    label_id = Label(janela_sub, text="ID:")
    label_id.pack()
    entrada_id = Entry(janela_sub)
    entrada_id.pack()

    botao_excluir = Button(janela_sub, text="Excluir", command=excluir)  # Cria um botão para excluir os dados
    botao_excluir.pack(anchor="center", padx=5, pady=5)  # Exclui o item com o ID fornecido

    def fechar_janela_subtracao():
        janela_sub.destroy()
        janela_init.deiconify()  # Mostra a janela inicial quando a janela de subtração for fechada

    janela_sub.protocol("WM_DELETE_WINDOW", fechar_janela_subtracao)  # Configura a ação ao fechar a janela

    centralizar_janela(janela_sub)  # Centraliza a janela inicial

    janela_sub.mainloop()  # Mantem a janela aberta, Último código da janela
#--------------------------------------------------------------------------------------------------------

#---------------------------------Função Exibir Cardapio--------------------------------------------------
def exibir_cardapio():
    # Tamanho do conjunto (quantidade de itens por linha)
    tamanho_conjunto = 3
    comando = f'SELECT * FROM hamburgeres'  # Comando a ser executado
    cursor.execute(comando)  # Execução do comando
    resultado = cursor.fetchall()  # Le os dados que foram requisitados

    # Função para formatar a lista com quebra de linha
    def formatar_lista(resultado, tamanho_conjunto):
        lista_formatada = ''
        for i, tupla in enumerate(resultado, start=1):
            lista_formatada += f"{tupla[0]} {tupla[1]} {tupla[2]}\n"  # Adiciona os valores da tupla à lista formatada
        return lista_formatada

    texto_final["text"] = formatar_lista(resultado, tamanho_conjunto)  # Define o texto da label como a lista formatada
#---------------------------------------------------------------------------------------------------------

#----------------------------------Função exibir edição--------------------------------------------------
def abrir_janela_edicao():
    # Esconder a janela inicial
    janela_init.withdraw()

    def editar_id():
        novo_valor = entrada_novo_valor.get()
        comando = f'UPDATE hamburgeres SET id_hamb = {novo_valor} WHERE id_hamb = {id_hamb}'  # Comando a ser executado
        cursor.execute(comando)  # Execução do comando
        conexao.commit()  # Commit/envio do comando para a database

    def editar_nome():
        novo_valor = entrada_novo_valor.get()
        comando = f'UPDATE hamburgeres SET nome_hamb = "{novo_valor}" WHERE id_hamb = {id_hamb}'  # Comando a ser executado
        cursor.execute(comando)  # Execução do comando
        conexao.commit()  # Commit/envio do comando para a database

    def editar_preco():
        novo_valor = entrada_novo_valor.get()
        comando = f'UPDATE hamburgeres SET preco_hamb = {novo_valor} WHERE id_hamb = {id_hamb}'  # Comando a ser executado
        cursor.execute(comando)  # Execução do comando
        conexao.commit()  # Commit/envio do comando para a database

    def selecionar_opcao(opcao):
        global id_hamb
        id_hamb = entrada_id.get()
        if opcao == "ID":
            editar_id()
        elif opcao == "Nome":
            editar_nome()
        elif opcao == "Preço":
            editar_preco()

        # Fechar a janela de edição após editar os dados
        janela_edi.destroy()
        janela_init.deiconify()  # Mostra a janela inicial quando a janela de edição for fechada

    # Janela de Edição
    janela_edi = Tk()  # Cria Janela
    janela_edi.title("Editar Item")  # Define o nome da Janela

    texto_inicial = Label(janela_edi, text="Hamburgueres", font=("Helvetica", 30), fg="red")  # Cria uma label de texto
    texto_inicial.pack(anchor="center", padx=10, pady=10)  # Define a posição da label

    texto_informativo = Label(janela_edi, text="Informe os valores e depois clique na opção desejada")  # Cria uma label de texto
    texto_informativo.pack(anchor="center", padx=10, pady=10)  # Define a posição da label

    # Campo de ID
    label_id = Label(janela_edi, text="ID:")
    label_id.pack()
    entrada_id = Entry(janela_edi)
    entrada_id.pack()

    # Campo para inserir o novo valor
    label_novo_valor = Label(janela_edi, text="Novo valor:")
    label_novo_valor.pack()
    entrada_novo_valor = Entry(janela_edi)
    entrada_novo_valor.pack()

    # Campo para selecionar o tipo de edição
    label_opcao = Label(janela_edi, text="Selecione o que deseja editar:")
    label_opcao.pack()

    # Frame para centralizar os botões horizontalmente
    frame_botoes = Frame(janela_edi)
    frame_botoes.pack()

    # Criação dos botões de opção
    opcoes = ["ID", "Nome", "Preço"]
    for opcao in opcoes:
        botao_opcao = Button(frame_botoes, text=opcao, command=lambda opcao=opcao: selecionar_opcao(opcao))
        botao_opcao.pack(side=LEFT, padx=5, pady=5)  # Organiza os botões um ao lado do outro

    # Centraliza o frame dos botões horizontalmente
    frame_botoes.pack(anchor=CENTER)

    def fechar_janela_edicao():
        janela_edi.destroy()
        janela_init.deiconify()  # Mostra a janela inicial quando a janela de edição for fechada

    janela_edi.protocol("WM_DELETE_WINDOW", fechar_janela_edicao)  # Configura a ação ao fechar a janela

    centralizar_janela(janela_edi)  # Centraliza a janela inicial

    janela_edi.mainloop()  # Mantem a janela aberta, Último código da janela
#--------------------------------------------------------------------------------------------------------

#--------------------------------Função Abrir Cardapio---------------------------------------------------
def abrir_janela_cardapio():
    # Esconder a janela inicial
    janela_init.withdraw()

    # Janela De cardápio
    janela_cardapio = Tk()  # Cria Janela
    janela_cardapio.title("Cardápio")  # Define o nome da Janela

    texto_inicial = Label(janela_cardapio, text="Hamburgueres", font=("Helvetica", 30), fg="red")  # Cria uma label de texto
    texto_inicial.pack(anchor="center", padx=10, pady=10)  # Define a posição da label

    botao = Button(janela_cardapio, text="Exibir", font=("Helvetica", 20), command=exibir_cardapio)  # Cria um botão
    botao.pack(anchor="center", pady=10, padx=10)  # Define a posição do Botão

    global texto_final
    texto_final = Label(janela_cardapio, text="", font=("Helvetica", 15), justify=LEFT)  # Cria uma label de texto variável com justificação à esquerda
    texto_final.pack(anchor="center", pady=10, padx=10)  # Define a posição da label

    def fechar_janela_cardapio():
        janela_cardapio.destroy()
        janela_init.deiconify()  # Mostra a janela inicial quando a janela de cardápio for fechada

    janela_cardapio.protocol("WM_DELETE_WINDOW", fechar_janela_cardapio)  # Configura a ação ao fechar a janela

    centralizar_janela(janela_cardapio)  # Centraliza a janela inicial

    janela_cardapio.mainloop()  # Mantem a janela aberta, Último código da janela
#------------------------------------------------------------------------------------------------------------

# Janela Inicial
janela_init = Tk()  # Cria Janela
janela_init.title("Hamburgeria")  # Define o nome da Janela

texto_inicial = Label(janela_init, text="Hamburgueria", font=("Helvetica", 30), fg="red")  # Cria uma label de texto
texto_inicial.pack(anchor="center", padx=10, pady=10)  # Define a posição da label

botao = Button(janela_init, text="Venda", font=("Helvetica", 30), command=abrir_janela_venda)  # Cria um botão
botao.pack(anchor="center", pady=10, padx=10)  # Define a posição do Botão

botao = Button(janela_init, text="Adição do cardapio", font=("Helvetica", 20), command=abrir_janela_adicao)  # Cria um botão
botao.pack(anchor="center", pady=10, padx=10)  # Define a posição do Botão

botao = Button(janela_init, text="Subtração do cardapio", font=("Helvetica", 20), command=abrir_janela_subtracao)  # Cria um botão
botao.pack(anchor="center", pady=10, padx=10)  # Define a posição do Botão

botao = Button(janela_init, text="Edição do cardapio", font=("Helvetica", 20), command=abrir_janela_edicao)  # Cria um botão
botao.pack(anchor="center", pady=10, padx=10)  # Define a posição do Botão

botao = Button(janela_init, text="Exibição do cardapio", font=("Helvetica", 20), command=abrir_janela_cardapio)  # Cria um botão
botao.pack(anchor="center", pady=10, padx=10)  # Define a posição do Botão

texto_final = Label(janela_init, text="", font=("Helvetica", 15))  # Cria uma label de texto variável
texto_final.pack(anchor="center", pady=10, padx=10)  # Define a posição da label

centralizar_janela(janela_init)  # Centraliza a janela inicial

janela_init.mainloop()  # Mantem a janela aberta, Ultimo código da janela
# ---------------------------------------------------------------------------------------------------------

# Janela De vendas
#janela = Tk()  # Cria Janela
#janela.title("Hamburgeria")  # Define o nome da Janela

#texto_inicial = Label(janela, text="Hamburgueres", font=("Helvetica", 30), fg="red")  # Cria uma label de texto
#texto_inicial.pack(anchor="center", padx=10, pady=10)  # Define a posição da label

#botao = Button(janela, text="Exibir", font=("Helvetica", 20), command=vendas)  # Cria um botão
#botao.pack(anchor="center", pady=10, padx=10)  # Define a posição do Botão

#texto_final = Label(janela, text="", font=("Helvetica", 15), justify=LEFT)  # Cria uma label de texto variável com justificação à esquerda
#$texto_final.pack(anchor="center", pady=10, padx=10)  # Define a posição da label

#janela.mainloop()  # Mantem a janela aberta, Último código da janela
# ---------------------------------------------------------------------------------------------------------

# Tremino da conexão com banco de dados
cursor.close()  # Fecha o cursor, último código do banco de dados
conexao.close()  # Fecha a conexão com o banco de dados, último código do banco de dados
# ---------------------------------------------------------------------------------------------------------
