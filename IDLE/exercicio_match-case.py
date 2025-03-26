# Escreva um programa em Python que leia o nome de um aluno e 3 notas. 
# O programa deve calcular a média e verificar se o aluno está aprovado ou reprovado.
# Para estar aprovado, o aluno deve ter média maior ou igual a 6.
# O programa deve determinar o conceito obtido pelo aluno, de acordo com a tabela abaixo:

# Conceito 'A' - media >= 9 E media <= 10
# Conceito 'B' - media >= 8 E media <= 9
# Conceito 'C' - media >= 7 E media <= 8
# Conceito 'D' - media >= 6 E media <= 7
# Conceito 'E' - media < 6

# O programa deve imprimir o nome do aluno, a média, o status e o
# conceito obtido - match_case (de acordo com o conceito)

nome_aluno = input('Nome: ')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))

media = (nota1 + nota2 + nota3) / 3


if media >= 9 and media <= 10:
    status = 'Aprovado'
    conceito = 'A' 
elif media >= 8 and media < 9:
    status = 'Aprovado'
    conceito = 'B' 
elif media >= 7 and media < 8:
    status = 'Aprovado'
    conceito = 'C' 
elif media >= 6 and media < 7:
    status = 'Aprovado'
    conceito = 'D'
else:
    status = 'Reprovado'
    conceito = 'E'


match conceito:
    case 'A':
        print(f'Nome: {nome_aluno}, você foi {status} com conceito {conceito} \nMédia: {media:.1f}')
    case 'B':
        print(f'Nome: {nome_aluno}, você foi {status} com conceito {conceito} \nMédia: {media:.1f}')
    case 'C':
        print(f'Nome: {nome_aluno}, você foi {status} com conceito {conceito} \nMédia: {media:.1f}')
    case 'D':
        print(f'Nome: {nome_aluno}, você foi {status} com conceito {conceito} \nMédia: {media:.1f}')
    case 'E':
        print(f'Nome: {nome_aluno}, você foi {status} com conceito {conceito} \nMédia: {media:.1f}')

            

