import random
def sortear_valores_inflacao(lista,quantidade):
    for i in range(quantidade):
        lista.append(random.randint(4,10))
def exibir_dados_inflacao(lista):
    for item in lista:
        print(item)

def calcular_min(lista):
    menor = lista[0]
    mes = 0
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            mes = i
    return menor, mes + 1

def calcular_max(lista):
    maior = lista[0]
    mes_maior = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            mes_maior = i
    return maior, mes_maior + 1


#simulando que 0 é janeiro, 1 é fevereiro e assim por diante
lista_inflacao = []


sortear_valores_inflacao(lista_inflacao, 12)
exibir_dados_inflacao(lista_inflacao)

#próprio do python
#descartando o primeiro ''
lista_meses = ['', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
valor_minimo, mes_minimo = calcular_min(lista_inflacao)
valor_maximo, mes_maximo = calcular_max(lista_inflacao)

print(f"Valor mínimo: {valor_minimo} no mês {lista_meses[mes_minimo]}")

print(f"Valor máximo: {valor_maximo} no mês {lista_meses[mes_maximo]}")