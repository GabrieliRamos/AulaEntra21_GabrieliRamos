#--- Exercício 1  - Funções
#--- Escreva uma função para cadastro de pessoa:
#---       a função deve receber três parâmetros, nome, sobrenome e idade
#---       a função deve salvar os dados da pessoa em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de pessoas com idade igual ou superior a 18 anos
#---       a função deve retornar uma mensagem caso a idade informada seja menor que 18
#---       caso a pessoa tenha sido cadastrada com sucesso deve ser retornado um id 
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada



lista_cadastro = []
id = None

def cadastro_pessoa (nome, sobrenome, idade):
    cadastro = {}
    if idade >= 18:
        global id
        cadastro['NOME'] = nome
        cadastro['SOBRENOME'] = sobrenome
        cadastro['IDADE'] = idade
        lista_cadastro.append(cadastro)
        id = len(lista_cadastro)
        cadastro['ID'] = id
        return id
    else:
        print('ERRO. MENOR DE IDADE')
        
def listar_pessoas ():
    print('\n','*'*30)
    print(' LISTA DE PESSOAS CADASTRADAS ')
    print('*'*30,'\n')
    for i in lista_cadastro:
        print(i)

def busca_id():
    id_desejado = int(input('\nDigite o id que deseja ver o cadastro da pessoa: '))
    id_desejado = id_desejado - 1
    tamanho = len(lista_cadastro) - 1
    if id_desejado < 0 or id_desejado > tamanho:
        print('ID inválido')
    else:
        print('\n',lista_cadastro[id_desejado])
    





    

