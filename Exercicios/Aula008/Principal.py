#--- Exercício 5  - Funções
#--- Escreva um programa para cadastro de pessoas e endereços:
#---       o programa deve solicitar os dados de pessoa utilizados na função do ex1
#---       o programa deve solicitar os dados de endereços utilizados na função do ex2
#---       o programa deve passar o id obtido na função do ex1 para a função do ex2
#---       o programa deve mostrar ao final os dados de todos as pessoas cadastradas com seus respectivos endereços utilizando as funções do ex3 e ex4

from Ex1Aula008 import cadastro_pessoa
from Ex1Aula008 import listar_pessoas
from Ex1Aula008 import busca_id
from Ex2Aula008 import cadastro_endereco
from Ex2Aula008 import listando_enderecos
from Ex2Aula008 import endereco_id

lista_cadastro = []
lista_endereco = []

quant_cadastros = int(input('\nDIGITE O NÚMERO DE PESSOAS QUE DESEJA CADASTRAR: '))

for i in range (quant_cadastros):
    print('\n','-'*5, 'CADASTRO DE PESSOA', '-'*5)

    nome = input('\nDigite seu nome: ')
    sobrenome = input('Digite seu sobrenome: ')
    idade = int(input('Digite sua idade: '))
    id_pessoa = cadastro_pessoa(nome, sobrenome, idade)

    print('\n','-'*5, 'CADASTRO DE ENDEREÇO', '-'*5)

    rua = input('\nDigite sua rua: ')
    numero = int(input('Digite o número: '))
    complemento = input('Digite o complemento: ')
    bairro = input('Digite seu bairro: ')
    cidade = input('Digite sua cidade: ')
    estado = input('Digite seu estado: ')

    print('\nSEU ID É: {}\n' .format(id_pessoa))

    cadastro_endereco(id_pessoa, idade, rua, numero, complemento, bairro, cidade, estado)
    

listar_pessoas()
listando_enderecos()
busca_id()
endereco_id()







