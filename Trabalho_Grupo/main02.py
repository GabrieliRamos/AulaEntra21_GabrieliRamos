import sqlite3

from criar_banco import *
from cadastro_carros02 import *
from cadastro_pessoas02 import *
from cadastro_unico import *

try:
    criar_banco()
except:
    print('Bancos de Dados já criados')

if __name__ == "__main__":


    while True:
        op = str(input(f'''
        {"-"*50}
        CADASTRO DE PESSOAS E AUTOMÓVEIS
        {"-"*50}
        SELECIONE A OPÇÃO DESEJADA:
        [1] - CADASTRO DE PESSOA
        [2] - CADASTRO DE AUTOMOVEL
        [3] - MOSTAR PESSOAS CADASTRADAS
        [4] - MOSTRAR CARROS CADASTRADOS
        [5] - MOSTRAR CARROS E PROPRIETÁRIOS
        [6] - ALTERAR DADOS
        [7] - SAIR
        '''))   
            
        

        if op == '1':

            print(f'{"-"*10} CADASTRO PESSOA {"-"*10}')
            nome_completo = input('Nome Completo: ')
            sexo = input('Sexo: ')
            data_nascimento = input('Data de Nascimento: ')
            cpf = input('CPF: ')
            rua = input('Rua: ')
            numero = input('Número: ')
            bairro = input('Bairro: ')
            cidade = input('cidade: ')
            estado = input('Estado: ')
            naturalidade = input('Naturalidade: ')
            nacionalidade = input('Nacionalidade: ')
            profissao = input('Profissão: ')
            salario = float(input('Salário: '))
            email = input('Email: ')
            telefone = input('Telefone: ')
                       

            pessoa = Pessoa(nome_completo,sexo,data_nascimento,cpf,rua,numero,bairro,cidade,estado,
            naturalidade,nacionalidade,profissao,salario,email,telefone)

            lista_pessoa = pessoa.lista
            
            conn = sqlite3.connect('cadastro02.db')
            cursor = conn.cursor()
            try:
            # inserindo dados na tabela através de parâmetros
                cursor.executemany("""
                INSERT INTO pessoa (nome_completo,sexo,data_nascimento,cpf,rua,numero,bairro,cidade,estado,
                    naturalidade,nacionalidade,profissao,salario,email,telefone)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """, lista_pessoa)
                conn.commit()
            except:
                # rollback all database actions since last commit
                conn.rollback()
                raise RuntimeError("Uh oh, an error occurred ...")

            print('Dados inseridos com sucesso.')
            conn.close()

        elif op == '2':

            print(f'\n{"-"*10} CADASTRO AUTOMOVEL {"-"*10}\n')
            id_pessoa_carro()
            print('\n')
            id_pessoa = input('Você precisa indicar o id da pessoa vinculada a este veículo: ')
            marca = input('Marca: ')
            modelo = input('Modelo: ')
            ano = int(input('Ano: '))
            placa = input('Placa: ')
            proprietario = input('Proprietario: ')
            num_portas = input('Número de portas: ')
            cor = input('Cor: ')
            km_rodado = input('Quilometragem: ')
            qtd_passageiros = input('Lugares: ')
            motor = input('Motorização: ')
            combustivel = input('Combustivel: ')
            meio_locomocao = input('Uso (Urbano/Rodoviario/Misto): ')
            valor = float(input('Valor: '))

            carro = Carro(id_pessoa,marca,modelo,ano,placa,proprietario,num_portas,cor,km_rodado,qtd_passageiros,
            motor,combustivel,meio_locomocao,valor)

            lista_carro = carro.lista
            
            conn = sqlite3.connect('cadastro02.db')
            cursor = conn.cursor()
            try:
            # inserindo dados na tabela através de parâmetros
                cursor.executemany("""
                INSERT INTO carro (id_pessoa,marca, modelo, ano, placa, proprietario, num_portas, cor, km_rodado, qtd_passageiros, motor,
                    combustivel, uso, valor)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """, lista_carro)
                conn.commit()
            except:
                # rollback all database actions since last commit
                conn.rollback()
                raise RuntimeError("Uh oh, an error occurred ...")

            print('Dados inseridos com sucesso.')
            conn.close()                

        elif op == '3':
            mostrar_pessoas()

        elif op == '4':
            mostrar_carros()

        elif op == '5':
            mostrar_pessoa_carro()

        elif op == '6':

            while True:

                opcao = str(input(f'''
                {"-"*50}
                ALTERAÇÃO DE DADOS DE PESSOAS E AUTOMÓVEIS
                {"-"*50}
                SELECIONE A OPÇÃO DESEJADA:
                [1] - ALTERAR DADOS DE PESSOA
                [2] - ALTERAR DADOS DE AUTOMÓVEL
                [3] - DELETAR DADOS DE PESSOA
                [4] - DELETAR DADOS DE AUTOMÓVEL
                [5] - SAIR
                '''))

                if opcao == '1':
                    mostrar_pessoas()
                    alterar_dados_pessoas()
                elif opcao == '2':
                    mostrar_carros()
                    alterar_dados_carro()
                elif opcao == '3':
                    mostrar_pessoas()
                    deletar_dado_pessoa()
                elif opcao == '4':
                    mostrar_carros()
                    deletar_dado_automovel()
                elif opcao == '5':
                    print(f'''
                    {"*"*50}
                    OBRIGADO POR UTILIZAR NOSSA APLICAÇÃO
                    v.001 
                    {"*"*50}
                    ''')
                    break
                else:
                    print('OPÇÃO INVÁLIDA')

        elif op == '7':
            print(f'''
            {"*"*50}
            OBRIGADO POR UTILIZAR NOSSA APLICAÇÃO
            v.001 
            {"*"*50}
            ''')
            break

        else:
            print('OPÇÃO INVÁLIDA')