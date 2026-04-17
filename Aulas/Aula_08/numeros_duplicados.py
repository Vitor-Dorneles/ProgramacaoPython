#// Data: 09/04/2026
#3. apagar numeros replicados
import random
lista_numeros = []

for i in range(10):
    numero_sorteado = random.randint(0,100)
    lista_numeros.append(numero_sorteado)
print(lista_numeros)

lista_numeros.sort() # para ordenar
print(lista_numeros)


print("Remoção de duplicados")
for n in lista_numeros:
    if n in lista_numeros:
        lista_numeros.remove(n)

print(lista_numeros)