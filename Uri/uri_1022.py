def main():

    N = int(input())
    
    for i in range(N):
        X1, operacao1, Y1, operacao_principal, X2, operacao2, Y2= input().split()
        X1 = int(X1)
        Y1 = int(Y1)
        X2 = int(X2)
        Y2 = int(Y2)

        if operacao_principal == '+':
            den_soma = (X1*Y2 + X2*Y1)
            nume_soma = (Y1*Y2)
        elif operacao_principal == '-':
            den_subt = (X1*Y2 - X2*Y1) 
            nume_subt = (Y1*Y2)
        elif operacao_principal == '*':
            den_multip = (X1*X2)
            nume_multip = (Y1*Y2)
        elif operacao_principal == '/':
            den_divisao = (X1*Y2)
            nume_divisao = (X2*Y1)

    while den_divisao>=1:
        if den_divisao%2==0:
            fat_divisao = den_divisao/2
            if den_divisao
    print(f'{den_soma}/{nume_soma} = ')
    print(f'{den_subt}/{nume_subt} = ')
    print(f'{den_multip}/{nume_multip} = ')
    print(f'{den_divisao}/{nume_divisao} = ')


if __name__ == '__main__':
    main()