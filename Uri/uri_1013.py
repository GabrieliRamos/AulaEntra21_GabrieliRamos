a, b, c = input().split()

MaiorAB = (int(a)+int(b)+abs(int(a)-int(b)))/2
maior = (MaiorAB+int(c)+abs(MaiorAB-int(c)))/2

print(f'{int(maior)} eh o maior')