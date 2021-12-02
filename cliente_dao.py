#DAO (data access object)
#centraliza o acesso aos dados dos objetos cliente

#Lista que ira armazenar todos os clientes do sistema
lista_clientes = []

#adicionar novo cliente
def adicionar(novo_cliente):
    lista_clientes.append(novo_cliente)

#pega um cliente pelo ID
def getCliente(id)
    for c in lista_clientes:
        if c.id == id.
              return c #return - retornar retornando o objeto definido

#Editar cliente - dado um objeto cliente, buscarna
#lista atraves do seu id e atualiza-lo
def editar(cliente):
    pass

#Excluir cliente dado o id do cliente remove-lo da lista
def excluir(id cliente):
    pass
   
#lista todos os clientes
def listar_todos():
    #passa por todos os clientes da listae
    #chama a função imprime() desses objetos
    for cliente in lista_clientes
    cliente.imprime()

#listar um cliente especifico