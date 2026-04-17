# lista e decomposiçao funcional
# criar um programa com método que popule N numeros aleatórios (100 a 200) em uma lista. Também crie método que exiba a lista. 
# O método a ser criado para avaliação, não pode ter pacotes, nem bibliotecas prontas do python.
# O método deve receber uma lista com números e retirar (da própria lista) todos os números replicados.
# Por exemplo, lista inicial = [6,4,2,6,9,2,6]
# lista transformada = [6,4,2,9]
# não usar bibliotecas para remover
#pode usar o random para gerar os números aleatorios
# enviar o link do github com a solução para alexz@ufn.edu.br

import random
def gerar_numeros_aleatorios(lista,quantidade): 
    for i in range(quantidade): #laço com os N números inseridos
        lista.append(random.randint(100,200)) 

def exibir_lista(lista):
    print(f"A lista é:")
    print(lista)

def remover_duplicados(lista):
    lista_sem_duplicadas = []
    for numero in lista:
        if numero not in lista_sem_duplicadas: # para verificar
            lista_sem_duplicadas.append(numero)
    return lista_sem_duplicadas

lista_numeros_inicial = []

gerar_numeros_aleatorios(lista_numeros_inicial, 15)

exibir_lista(lista_numeros_inicial)

nova_lista = remover_duplicados(lista_numeros_inicial)

exibir_lista(nova_lista)