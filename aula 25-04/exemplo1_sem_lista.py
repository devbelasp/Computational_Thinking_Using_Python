'''
Crie um programa em python que recebe como entrada quatro salários,o programa 
deve calcular a média salarial e exibir os salários que estão abaixo da média.
'''

soma = 0
salario_0 = float(input('Salário R$: '))
soma += salario_0
salario_1 = float(input('Salário R$: '))
soma += salario_1
salario_2 = float(input('Salário R$: '))
soma += salario_2
salario_3 = float(input('Salário R$: '))
soma += salario_3

media = soma / 4
print(f'Média salarial: {media:.2f}')

if salario_0 < media:
    print(f'Salário abaixo da média: {salario_0:.2f}')
if salario_1 < media:
    print(f'Salário abaixo da média: {salario_1:.2f}')
if salario_2 < media:
    print(f'Salário abaixo da média: {salario_2:.2f}')
if salario_3 < media:
    print(f'Salário abaixo da média: {salario_3:.2f}')