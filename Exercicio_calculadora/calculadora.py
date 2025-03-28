# Calculadora da Isa ♥

print('Vamos calcular dois números inteiros')
numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))

print('------------------')
print('Menu de operações:')
print('1. Soma')
print('2. Subtração')
print('3. Multiplicação')
print('4. Divisão')
print('5. Potência')
print('-------------------')

operacao_escolhida = input('Escolha sua operação (1,2,3,4 ou 5): ')

if operacao_escolhida == '1':
        soma = numero1 + numero2
        print(f' A soma do número {numero1} + {numero2} é igual a: {soma}')
elif operacao_escolhida == '2':
    sub = numero1 - numero2
    print(f' A subtração do número {numero1} - {numero2} é igual a: {sub}')
elif operacao_escolhida == '3':
    multi = numero1 * numero2
    print(f' A multiplicação do número {numero1} * {numero2} é igual a: {multi}')
elif operacao_escolhida == '4':
    div = numero1 / numero2
    print(f' A divisão do número {numero1} / {numero2} é igual a: {div}')
elif operacao_escolhida == '5':
    potencia = numero1 ** numero2
    print(f' A potência do número {numero1} ** {numero2} é igual a: {potencia}')
else:
    print('Não entendi, digite novamente.')

print('Muito obrigada!')