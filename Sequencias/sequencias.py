Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Listas
>>> #construtor list()
>>> #mutável e heterogênea
>>> 
>>> lista = list()
>>> lista
[]
>>> type(lista)
<class 'list'>
>>> lista = []
>>> lista
[]
>>> lista = [3, True, 3.14, 'Python']
>>> lista
[3, True, 3.14, 'Python']
>>> len(lista)
4
>>> lista[2] = 3.16
>>> lista
[3, True, 3.16, 'Python']
>>> lista[0] = 20
>>> lista
[20, True, 3.16, 'Python']
>>> lista[3] = 'Java'
>>> lista
[20, True, 3.16, 'Java']
>>> type(lista)
<class 'list'>
>>> 
>>> #Tupla
>>> #Imutável e heterogênea
... #construtor tuple()
>>> 
>>> tupla = tuple()
>>> tupla
()
>>> type(tupla)
<class 'tuple'>
>>> tupla = ()
tupla
()
type(tupla)
<class 'tuple'>
tupla = (123)
tupla
123
type(tupla)
<class 'int'>
tupla = (123,)
tupla
(123,)
type(tupla)
<class 'tuple'>
tupla = (123, True, 3.14, 'Python')
tupla
(123, True, 3.14, 'Python')
len(tupla)
4
tupla[1]
True
tupla[3]
'Python'
i = 0
while i<len(tupla):
    print(tupla[i])
    i+=1

123
True
3.14
Python

#Strings
#imutáceis e homogêneas

texto = 'Linguagem'

i = 0
while i<len(texto):
    print(texto[i])
    i+=1

L
i
n
g
u
a
g
e
m

#intervalo -> range()
#imutáveis e homogênea
#construtor -> range()
 
# três parâmetros - range(inicio, fim, passo)
# dois parâmetros - range(inicio, fim)
# um parâmetro - range(fim)

intervalo = range(0)
intervalo
range(0, 0)
intervalo = range(5, 10, 2)
intervalo
range(5, 10, 2)
lista = list(intervalo)
lista
[5, 7, 9]
tupla = tuple(intervalo)
tupla
(5, 7, 9)
intervalo[0]
5
tupla[0]
5
intervalo[0] = 70
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    intervalo[0] = 70
TypeError: 'range' object does not support item assignment
