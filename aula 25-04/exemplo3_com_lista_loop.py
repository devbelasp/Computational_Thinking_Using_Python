'''
Crie um programa em python que recebe como entrada quatro salários,o programa 
deve calcular a média salarial e exibir os salários que estão abaixo da média.
'''

salarios = [0, 0, 0, 0]
soma = 0
i = 0 #controle do looping
#preenchendo a lista salarios
while i < 4:
    salarios[i] = float(input('Salário R$: '))
    soma += salarios [i]
    i+=1

#calcular a media
media = soma/4

print(f'Média Salarial: {media:.2f}')

#imprimir os salários que estão abaixo da média
i = 0
while i < 4:
    if salarios[i] < media:
        print(f'Salário abaixo da média: {salarios[i]:.2f}')
    i+=1