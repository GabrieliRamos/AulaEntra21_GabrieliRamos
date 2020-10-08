A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
pi = 3.14159

area_triangulo = (A*C)/2
area_circulo = (pi * (C**2))
area_trapezio = ((A+B)*C)/2
area_quadrado = (B*B)
area_retangulo = (A*B)

print('TRIANGULO: %.3f'%area_triangulo)
print('CIRCULO: %.3f'%area_circulo)
print('TRAPEZIO: %.3f'%area_trapezio)
print('QUADRADO: %.3f'%area_quadrado)
print('RETANGULO: %.3f'%area_retangulo)