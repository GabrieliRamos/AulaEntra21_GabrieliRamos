def main():

    N = int(input())
    
    for i in range(N):
        F1, F2 = input().split()
        F1 = int(F1)
        F2 = int(F2)

        if F1 > F2:
            resultado = F1%F2
        else:
            resultado = F2%F1
    print(resultado)


if __name__ == '__main__':
    main()