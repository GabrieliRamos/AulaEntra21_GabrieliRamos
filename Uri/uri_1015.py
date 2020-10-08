def main():
    import math

    x1, y1 = input().split()
    x2, y2 = input().split()

    z = ((float(x2) - float(x1))**2) + ((float(y2) - float(y1))**2)
    distancia = math.sqrt(z)
    print('%.4f'%distancia)

if __name__ == '__main__':
    main()