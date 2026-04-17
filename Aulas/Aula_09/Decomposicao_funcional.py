#// Data: 16/04/2026

#Decomposição Funcional

import random

#método em forma de função ou procedimento
def popular_lista(lista, quantidade):
    for i in range(quantidade):
        lista.append(random.randint(1,100))

#método em forma de função ou procedimento
def exibir_lista(lista):
   for item in lista:
    print(item)

def copiar_numeros(lista_numeros, lista_pares, lista_impares):
   for numero in lista_numeros:
     if numero % 2 == 0:
         lista_pares.append(numero)
     else:
        lista_impares.append(numero)

lista_numeros_aleatorios = [] #declaração
lista_pares = []
lista_impares = []

#acionando ou invocando um método que tem o serviço de popular uma lista com n números
#ao utilizarmos métodos, estamos usando DECOMPOSIÇÃO FUNCIONAL

#DECOMPOSIÇÃO FUNCIONAL seria a separação de todos os métodos que sabem fazer serviços
popular_lista(lista_numeros_aleatorios, 10)

exibir_lista(lista_numeros_aleatorios)

copiar_numeros(lista_numeros_aleatorios, lista_pares, lista_impares)

print("numeros pares")
exibir_lista(lista_pares)
print("numeros impares")
exibir_lista(lista_impares)