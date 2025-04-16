#23:58:55 -> ALARME!
##Solicitar ao usuário o horário do alarme
#Homework - Adicionar o dia da semana / validar as entradas
 
ha = int(input('Hora(s): '))
ma = int(input('Minuto(s): '))
sa = int(input('Segundo(s): '))
 
h = 0
while h <= 23:
    m = 0
    while m <= 59:
        s = 0
        while s <= 59:
            print(f'{h:02}:{m:02}:{s:02}')
            if h == ha and m == ma and s == sa:
                print('ALARME!')
                break
            s+=1
        if h == ha and m == ma:
            break   
        m+=1
    if h == ha:
        break    
    h+=1 
          
 
   