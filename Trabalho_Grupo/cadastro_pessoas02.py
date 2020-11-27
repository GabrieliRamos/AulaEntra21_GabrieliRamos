import sqlite3

class Pessoa():
        def __init__(self,nome_completo,sexo,data_nascimento,cpf,rua,numero,bairro,cidade,estado,naturalidade,nacionalidade
        ,profissao,salario,email,telefone):
                self.lista = []
                self.nome_completo = nome_completo
                self.sexo = sexo
                self.data_nascimento = data_nascimento
                self.cpf = cpf
                self.rua = rua
                self.numero = numero
                self.bairro = bairro
                self.cidade = cidade
                self.estado = estado
                self.naturalidade=naturalidade
                self.nacionalidade=nacionalidade
                self.profissao=profissao
                self.salario=salario
                self.email=email
                self.telefone=telefone
                self.tupla = (self.nome_completo,self.sexo,self.data_nascimento,self.cpf,self.rua,self.numero,
                self.bairro,self.cidade,self.estado,self.naturalidade,self.nacionalidade,self.profissao,self.salario,
                self.email,self.telefone)
                self.lista.append(self.tupla)

def mostrar_pessoas():
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
            Rua: {linha[5]}
            Número: {linha[6]}
            Bairoo: {linha[7]}
            Cidade: {linha[8]}
            Estado: {linha[9]}
            Cidade de Naturalidade: {linha[10]}
            Nacionalidade: {linha[11]}
            Profissão: {linha[12]}
            Salário: {linha[13]:.3f}
            Email: {linha[14]}
            Telefone: {linha[15]}
            {"******"*20})
        ''')
    conn.close()

def alterar_dados_pessoas():
    idp = int(input('Informe o id da pessoa desejada: '))
    conn = sqlite3.connect('cadastro02.db')
    cursor = conn.cursor()
    
    print(''' CAMPOS DE CADASTRO:
    - nome_completo
    - sexo
    - data_nascimento
    - cpf
    - rua
    - numero
    - bairro
    - cidade
    - estado
    - naturalidade
    - nacionalidade
    - profissao
    - salario
    - email
    - telefone
    ''')
    campo = str(input('DIGITE O CAMPO QUE DESEJA ALTERAR: '))
    novo_dado = input('INFORME O NOVO VALOR: ')

    

    cursor.execute(f"""
    UPDATE pessoa
    SET {campo} = ?
    WHERE id = ?
    """, (novo_dado, idp))

    conn.commit()

    print('Dados atualizados com sucesso.')

    conn.close()

def deletar_dado_pessoa():
    try:
        conn = sqlite3.connect('cadastro02.db')
        cursor = conn.cursor()
        id_cliente = input('Informe o id do ciente que deseja apagar: ')
        cursor.execute("""DELETE FROM pessoa WHERE id = ?""", (id_cliente,))
        conn.commit()
        print("Cliente excluido com sucesso!!!")
        conn.close()
    except:
        print("Cliente inexistente/já excluido.")

    
