# classe principal
#import - importa funções, variaveis, classes de outros arquivos
from model.cliente import Cliente

#carrega o arquivo do diretorio model/cliente dao.py
#e define um apelido chamando funcoes clentes para prover
#acesso as funçoes definidas no arquivo importado
import model.cliente_dao as funcoes clientes

#adiciona varios clientes
for i in range(0, 5):
    novo_cliente = Cliente(i, f'Cliente{i}' , 'rua a', '75 9 8888888')
    funcoes_clientes.adicionar(novo_cliente)
    
funcoes_clientes.listas_todos()

id_cliente = int(input("Digite o ID do cliente que deseja excluir: "))
funcoes_clientes.excluir(id_cliente)