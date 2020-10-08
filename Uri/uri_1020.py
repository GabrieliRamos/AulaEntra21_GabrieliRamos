def main():

    idade_dias = int(input())
    
    anos = idade_dias/365
    resto = idade_dias%365
    mes = resto/30
    dias = resto%30 

    print(f'{int(anos)} ano(s)')
    print(f'{int(mes)} mes(es)')
    print(f'{int(dias)} dia(s)')

if __name__ == '__main__':
    main()