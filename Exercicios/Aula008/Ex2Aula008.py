#--- Exercício 2  - Funções
#--- Escreva uma função para cadastro de endereço:
#---       a função deve receber sete parâmetros, id da pessoa, rua, numero, complemento, bairro, cidade e estado
#---       a função deve salvar os dados de endereço em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de endereços com todos os dados preenchidos
#---       a função deve retornar uma mensagem ao final de acordo com a situação
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada

lista_endereco = []

def cadastro_endereco(id_pessoa, idade, rua, numero:int, complemento, bairro, cidade, estado):
    cadastro = {}
    
    if ((idade < 18) and (rua == '' or complemento == '' or bairro == '' or cidade == '' or estado == '')):
        print('MENOR DE IDADE. \nERRO. Todos os dados devem ser preenchidos.') 
    elif ((idade < 18) and (rua == rua and numero == numero and complemento == complemento and bairro == bairro and cidade == cidade and estado == estado)):
        print('ERRO.MENOR DE IDADE. \nNÃO É POSSÍVEL CONTINUAR O CADASTRO\n')
    elif ((idade >= 18) and (rua == '' or complemento == '' or bairro == '' or cidade == '' or estado == '')):
        print('ERRO. Todos os dados devem ser preenchidos.')    
    else:
        cadastro['RUA'] = rua
        cadastro['NUMERO'] = numero
        cadastro['COMPLEMENTO'] = complemento
        cadastro['BAIRRO'] = bairro
        cadastro['CIDADE'] = cidade
        cadastro['ESTADO'] = estado
        lista_endereco.append(cadastro)
        print('=-'*10,'CADASTRO CONCLUÍDO', '-='*10, '\n')

def listando_enderecos():
    print('\n','*'*30)
    print('LISTA DE ENDEREÇOS CADASTRADOS')
    print('*'*30, '\n')
    for i in lista_endereco:
        print(i)

def endereco_id():
    id_busca = int(input('\nDigite o id que deseja ver o cadastro de endereço: '))
    id_busca = id_busca - 1
    tamanho = len(lista_endereco) - 1
    if id_busca < 0 or id_busca > tamanho:
        print('ID inválido')
    else:
        print(lista_endereco[id_busca])

