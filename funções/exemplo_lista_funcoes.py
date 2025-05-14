'''
Manipulação de Listas com funções
Documentação docstrings

1) Funcção para definir o tamanho da lista
2) Função para preencher a lista
3) Função para percorrer e imprimir os elementos da lista
4) Função para somar todos os elementos da lista
5) Função para imprimir os elementos pares da lista
6) Função para imprimir os elementos ímpares da lista
...
7) Função principal para testar o programa
'''

def tamanho_lista():
    """
    Obter e retornar o tamanho da lista (número inteiro)

    Parêmetros
    --------------------------------------------------------
    - função sem parâmetros

    Retorno
    --------------------------------------------------------
    - retornar o valor de t - tamanho da lista
    """

    print('*-- TAMANHO da LISTA --*')
    print('------------------------')
    t = int(input('Tamanho: '))
    return t

def criar_lista(t):
    print(f'*-- CRIANDO uma LISTA com {t} ELEMENTOS --*')
    print('--------------------------------------------')
    lista = [] #criando uma lista
    i=0 #variável de controle da repetição

    while i<t:
        n = int(input('Número: '))
        lista.append(n)
        i+=1
    return lista

def somatorio(lista):
    print('*-- SOMANDO todos os ELEMENTOS da LISTA --*')
    print('-------------------------------------------')
    soma = 0
    for n in lista:
        soma += n
    return soma

def imprimir_pares(lista):
    print('*-- IMPRIMINDO os ELEMENTOS PARES --*')
    print('-------------------------------------')
    for n in lista:
        if n % 2 == 0:
            print(f'{n} é PAR!')

def imprimir_impares(lista):
    print('*-- IMPRIMINDO os ELEMENTOS ÍMPARES --*')
    print('---------------------------------------')
    for n in lista:
        if n % 2 == 1:
            print(f'{n} é ÍMPAR!')

def separar_pares(lista):
    print('*-- SEPARANDO os ELEMENTOS PARES --*')
    print('------------------------------------')
    lista_pares = []
    for n in lista:
        if n % 2 == 0:
            lista_pares.append(n)
    return lista_pares


def imprimir(lista):
    print('*-- IMPRIMINDO os ELEMENTOS da LISTA --*')
    print('----------------------------------------')
    for n in lista:
        print(f'Número: {n}')

def principal():
    print('--------------------------')
    print('*-- PROGRAMA PRINCIPAL --*')
    print('--------------------------')
    t = tamanho_lista()
    lista = criar_lista(t)
    imprimir(lista)
    print(f'Soma: {somatorio(lista)}')
    imprimir_pares(lista)
    imprimir_impares(lista)
    print(f'LISTA: {separar_pares(lista)}')

#Principal
principal()

