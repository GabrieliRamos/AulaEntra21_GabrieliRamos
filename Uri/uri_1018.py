def main():

    N = int(input())
    cem = N/100
    resto = N%100
    cinq = resto/50
    resto = resto%50
    vint = resto/20
    resto = resto%20
    dez = resto/10
    resto = resto%10
    cin = resto/5
    resto = resto%5
    dois = resto/2
    resto = resto%2
    um = resto

    print(N)
    print(f'{int(cem)} nota(s) de R$ 100,00')
    print(f'{int(cinq)} nota(s) de R$ 50,00')
    print(f'{int(vint)} nota(s) de R$ 20,00')
    print(f'{int(dez)} nota(s) de R$ 10,00')
    print(f'{int(cin)} nota(s) de R$ 5,00')
    print(f'{int(dois)} nota(s) de R$ 2,00')
    print(f'{int(um)} nota(s) de R$ 1,00')

if __name__ == '__main__':
    main()