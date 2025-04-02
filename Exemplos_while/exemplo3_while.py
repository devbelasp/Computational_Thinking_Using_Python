executa = input('Executa? (sim ou não): ')
cont = 0
while executa == 'sim': #variável controladora
    cont += 1 #variável acumuladora
    executa = input('Executa novamente? (sim ou não): ')

print (f'O bloco do while executou {cont} vezes!')