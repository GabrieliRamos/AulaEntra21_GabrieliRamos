import sqlite3

class Carro:
    def __init__(self,id_pessoa,marca,modelo,ano,placa,proprietario,num_portas,cor,km_rodado,qtd_passageiros,motor,combustivel,uso,valor):
        self.lista = []
        self.id_pessoa = id_pessoa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.proprietario = proprietario
        self.num_portas = num_portas
        self.cor = cor
        self.km_rodado = km_rodado
        self.qtd_passageiros = qtd_passageiros
        self.motor = motor
        self.combustivel = combustivel
        self.uso = uso
        self.valor = valor
        self.tupla = (self.id_pessoa,self.marca,self.modelo,self.ano,self.placa,self.proprietario,self.num_portas,
        self.cor,self.km_rodado,self.qtd_passageiros,self.motor,self.combustivel,self.uso,self.valor)
        self.lista.append(self.tupla)
        
def mostrar_carros():
    conn = sqlite3.connect('cadastro02.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM carro;
    """)

    for linha in cursor.fetchall():
        print(f'''
            \n
            {"******"*20}
            ID automóvel: {linha[0]}
            ID proprietário: {linha[1]}
            Marca: {linha[2]}
            Modelo: {linha[3]}
            Ano: {linha[4]}
            Placa: {linha[5]}
            Proprietario: {linha[6]}
            Número de portas: {linha[7]}
            Cor: {linha[8]}
            Quilometragem: {linha[9]}
            Lugares: {linha[10]}
            Motorização: {linha[11]}
            Combustivel: {linha[12]}
            Uso: {linha[13]}
            Valor: {linha[14]:.3f}
            {"******"*20}
        ''')

    conn.close()

def id_pessoa_carro():
    conn = sqlite3.connect('cadastro02.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM pessoa;
    """)

    for linha in cursor.fetchall():
        print(f'''
            \n
            {"******"*20}
            ID Pessoa: {linha[0]}
            Nome Completo: {linha[1]}
            Sexo: {linha[2]}
            Data Nascimento: {linha[3]}
            CPF: {linha[4]}
            
        ''')
    conn.close()

def alterar_dados_carro():
    idc = int(input('Informe o id do carro desejado: '))
    conn = sqlite3.connect('cadastro02.db')
    cursor = conn.cursor()
    
    print(''' CAMPOS DE CADASTRO:
    - id_pessoa
    - marca
    - modelo
    - ano
    - placa
    - proprietario
    - num_portas
    - cor
    - km_rodado
    - qtd_passageiros
    - motor
    - combustivel
    - meio_locomocao
    - valor
    escreva o nome do campo que deseja alterar: ''')
    campo = str(input('DIGITE O CAMPO QUE DESEJA ALTERAR: '))
    novo_dado = input('INFORME O NOVO VALOR: ')

    

    cursor.execute(f"""
    UPDATE carro
    SET {campo} = ?
    WHERE id = ?
    """, (novo_dado, idc))

    conn.commit()

    print('Dados atualizados com sucesso.')

    conn.close()

def deletar_dado_automovel():
    conn = sqlite3.connect('cadastro02.db')
    cursor = conn.cursor()
    id_carro = input('Informe o id do carro que deseja apagar: ')
    cursor.execute("""DELETE FROM carro WHERE id = ?""", (id_carro,))
    conn.commit()
    print("Carro excluido com sucesso!!!")
    conn.close()