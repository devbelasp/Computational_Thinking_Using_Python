'''
Crie um programa em python que recebe como entrada quatro salários,o programa 
deve calcular a média salarial e exibir os salários que estão abaixo da média.
'''

salarios = [0,0,0,0]

soma = 0
salarios[0]= float(input('Salário R$: '))
soma += salarios[0]
salarios[1] = float(input('Salário R$: '))
soma += salarios[1]
salarios[2] = float(input('Salário R$: '))
soma += salarios[2]
salarios[3] = float(input('Salário R$: '))
soma += salarios[3]

media = soma / 4
print(f'Média salarial: {media:.2f}')

if salarios[0] < media:
    print(f'Salário abaixo da média: {salarios[0]:.2f}')
if salarios[1] < media:
    print(f'Salário abaixo da média: {salarios[1]:.2f}')
if salarios[2] < media:
    print(f'Salário abaixo da média: {salarios[2]:.2f}')
if salarios[3] < media:
    print(f'Salário abaixo da média: {salarios[3]:.2f}')