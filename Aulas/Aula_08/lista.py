import random
lista_numeros = []
lista_nomes = []

lista_numeros.append(5)
lista_numeros.append(3)
lista_numeros.append(1)
print(lista_numeros)

for i in range(5):
    numero_sorteado = random.randint(0,100)
    lista_numeros.append(numero_sorteado)
print(lista_numeros)

lista_numeros.sort() # para ordenar
print(lista_numeros)

numero_pesquisa =int(input("Digite um número para pesquisar e remover: "))




if(numero_pesquisa in lista_numeros):
    print(f"Número está na lista {numero_pesquisa}")
    lista_numeros.remove(numero_pesquisa)
else:
    print("O número não está na lista")

print(lista_numeros)

# achar min e max
# fazer a média
numero_minimo = 0
if lista_numeros:
    numero_minimo = lista_numeros[0]
    for n in lista_numeros:
        if n < numero_minimo:
            numero_minimo = n
    print(numero_minimo)
else:
    print("Lista vazia")

numero_maximo = 0
if lista_numeros:
    numero_maximo = lista_numeros[0]
    for n in lista_numeros:
        if n > numero_maximo:
            numero_maximo = n
        print(numero_maximo)
else:
    print("Lista vazia")

tam = len(lista_numeros)

if tam > 0:
    soma = 0
    for n in lista_numeros:
        soma += n
    media = soma / tam
    print("Soma:", soma)
    print(f"Média: {media:.2f}")
else:
    print("Lista vazia")