print('Exemplo com if-elif-else')
print('------------------------')

final_placa = int(input('Número: '))

if final_placa == 1 or final_placa == 2:
    print('Segunda-feira')
elif final_placa == 3 or final_placa == 4:
    print('Terça-feira')
elif final_placa == 5 or final_placa == 6:
    print('Quarta-feira')
elif final_placa == 7 or final_placa == 8:
    print('Quinta-feira')
elif final_placa == 9 or final_placa == 0:
    print('Sexta-feira')
else:
    print('número inválido')

print('\nExemplo com match-case')
print('------------------------')
final_placa = int(input('Número: '))

match final_placa:
    case 1|2:
        print('Segunda-feira')
    case 3|4:
        print('Terça-feira')
    case 5|6:
        print('Quarta-feira')
    case 7|8:
        print('Quinta-feira')
    case 9|0:
        print('Sexta-feira')
    case _:
        print('número inválido')















        
        






