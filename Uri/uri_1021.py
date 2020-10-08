def main():

    N, M = (input().split('.'))
    M = float(M)
    N = float(N)

    #NOTAS
    cem = N//100
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

    #MOEDAS
    moeda_um_real = resto/1

    moeda_cinq = M/50
    resto = M%50

    moeda_vinte_cinco = resto/25
    resto = resto%25

    moeda_dez = resto/10
    resto = resto%10

    moeda_cinco = resto/5
    resto = resto%5

    moeda_um = resto


    print('NOTAS:')
    print(f'{int(cem)} nota(s) de R$ 100.00')
    print(f'{int(cinq)} nota(s) de R$ 50.00')
    print(f'{int(vint)} nota(s) de R$ 20.00')
    print(f'{int(dez)} nota(s) de R$ 10.00')
    print(f'{int(cin)} nota(s) de R$ 5.00')
    print(f'{int(dois)} nota(s) de R$ 2.00')
    print('MOEDAS:')
    print(f'{int(moeda_um_real)} moeda(s) de R$ 1.00')
    print(f'{int(moeda_cinq)} moeda(s) de R$ 0.50')
    print(f'{int(moeda_vinte_cinco)} moeda(s) de R$ 0.25')
    print(f'{int(moeda_dez)} moeda(s) de R$ 0.10')
    print(f'{int(moeda_cinco)} moeda(s) de R$ 0.05')
    print(f'{int(moeda_um)} moeda(s) de R$ 0.01')

if __name__ == '__main__':
    main()