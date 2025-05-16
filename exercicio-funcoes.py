'''
Escreva um programa em Python que leia n salários e armazene-os em uma lista.
O programa deve imprimir a média salárial e os salários que estiverem abaixo
da média. Para isso, escreva:

1) Função para obter o número de salários
2) Função para criar a lista de salários
3) Função para calcular a média salarial
4) Função para imprimir os salários abaixo da média
5) Função que retorne o maior salário
6) Função de teste
'''

def qtde_salarios():
    print('*-- Quantidade de salários --*')
    qtde = int(input('Qtde: '))
    return qtde

def criar_lista(qtde):
    print(f'*-- Criando uma lista com {qtde} itens --*')
    salarios = []
    i = 0
    while i < qtde:
        salario = float(input('Salário: '))
        salarios.append(salario)
        i+=1
    return salarios

def calcular_media(salarios):
    print(f'*-- Calcular a Média --*')
    soma = 0
    for salario in salarios:
        soma += salario
    media = soma / len(salarios)
    return media

def imprimir(salarios, media):
    print('*-- Imprimindo os salários abaixo da média --*')
    for salario in salarios:
        if salario < media:
            print(f'Abaixo da média: {salario:.2f}')

def obter_maior_salario(salarios):
    print('*-- Maior salário --*')
    maior = 0
    for salario in salarios:
        if salario > maior:
            maior = salario
    return maior

#Principal
qtde = qtde_salarios()
salarios = criar_lista(qtde)
media = calcular_media(salarios)
imprimir(salarios, media)
print(f'Maior: {obter_maior_salario(salarios)}')

