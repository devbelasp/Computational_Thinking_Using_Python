'''
Calculadora Simples
- Operações básicas: adição, subtração, divisão e multiplicação

Programa:
- menu()
- entrada_dados()
- adição()
- subtração()
- multiplicação()
- divisão()
- imprimir()
- controlador()
'''

#Função menu()
def menu():
    print('*-- Menu --*')
    print('------------')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    op = int(input('Operação:'))
    return op

#Função entrada_dados()
def entrada_dados():
    print('*-- Entrada de Dados --*')
    print('------------------------')
    num = int(input('Número: '))
    return num

#Função adicao()
def adicao(n1,n2):
    print('*-- Adição --*')
    print('--------------')
    result = n1 + n2
    return result

#Função subtracao()
def subtracao(n1,n2):
    print('*-- Subtração --*')
    print('-----------------')
    result = n1 - n2
    return result

#Função multiplicacao()
def multiplicacao(n1,n2):
    print('*-- Multiplicação --*')
    print('---------------------')
    result = n1 * n2
    return result

#Função divisao()
def divisao(n1,n2):
    print('*-- Divisão --*')
    print('---------------')
    result = n1 / n2
    return result

#Função imprimir()
def imprimir(resultado):
    print('***- Imprimindo o resultado... -***')
    print('===================================')
    print(f'Resultado: {resultado}')
    print('===================================')

#Função controlador()
def controlador(op, n1, n2):
    print('*-- Controlador --*')
    print('-------------------')
    if op == 1:
        result = adicao(n1,n2)
    elif op == 2:
        result = subtracao(n1, n2)
    elif op == 3:
        result = multiplicacao(n1, n2)
    elif op == 4:
        result = divisao(n1, n2)
    return result

#Principal
print('*** PRINCIPAL ***')
op = menu()
n1 = entrada_dados()
n2 = entrada_dados()
result = controlador(op, n1, n2)
imprimir(result)



