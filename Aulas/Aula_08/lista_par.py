# Data: 09/04/2026
#2. apagar todos os valores pares
import random
lista_numeros = []

for i in range(10):
    numero_sorteado = random.randint(0,10)
    lista_numeros.append(numero_sorteado)
print(lista_numeros)

lista_numeros.sort() # para ordenar
print(lista_numeros)

for n in lista_numeros:
    if n % 2 == 0:
        lista_numeros.remove(n)

print(lista_numeros)