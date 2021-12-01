#DAO (data access object)
#centraliza o acesso aos dados dos objetos cliente

#Lista que ira armazenar todos os clientes do sistema
lista_clientes = []

#adicionar novo cliente
def adicionar(novo_cliente):
    lista_clientes.append(novo_cliente)

#editar cliente
def edit():
    pass

#excluir liste
def delete():
    pass

#listar todos os cliente
def listaAll():
    for c in lista_clientes:
        c.print()


#pegar um clilente especifico
def lista_cliente():
    pass