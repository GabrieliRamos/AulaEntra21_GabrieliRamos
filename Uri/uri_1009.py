nome_funcionario = str(input())
salario_fixo = float(input())
venda_total = float(input())

salario_final = ((venda_total*(15/100)+salario_fixo))

print('TOTAL = R$ %.2f'%salario_final)