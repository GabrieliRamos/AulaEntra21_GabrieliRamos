def main():

    N = int(input())

    horas = N//3600
    resto = N%3600 
    minutos = (resto - horas)//60
    segundos = resto%60
    
    print(f'{int(horas)}:{int(minutos)}:{int(segundos)}')

if __name__ == '__main__':
    main()
