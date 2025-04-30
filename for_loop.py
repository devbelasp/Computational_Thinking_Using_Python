# Escreva um programa que leia 5 nomes, exiba a quantidade
# que iniciam com vogal e armazene esses nomes em uma lista (e os exiba)

#Criando uma lista vazia
nomes = []
nomes_vogal= []

#Preenchendo a lista com os nomes
for i in range(5):
    nome = input('Nome: ')
    nomes.append(nome)

#Variável contadora
qtde = 0


#Percorrer a lista de nomes, verificando as iniciadas com VOGAL
for nome in nomes:
    if nome[0] == 'A' or nome[0] == 'E' or nome[0] == 'I' or nome[0] == 'O' or nome[0] == 'U':
        qtde+=1
        nomes_vogal.append(nome)

# imprimindo as informações
print(f'Qtde de nomes que iniciam com VOGAL: {qtde}')
print(nomes_vogal)

print('-------------------------------------------------')

# percorrendo a lista e acessando os elementos um por um
print('Nome iniciados com VOGAL:')
for nome in nomes_vogal:
    print(f'Nome: {nome}')

