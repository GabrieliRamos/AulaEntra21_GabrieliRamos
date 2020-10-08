def main():

    tempo = int(input())
    velocidade_media = int(input())
    km_l_automovel = 12

    quant_litros = (velocidade_media/km_l_automovel)*tempo

    print('%.3f'%quant_litros)

if __name__ == '__main__':
    main()