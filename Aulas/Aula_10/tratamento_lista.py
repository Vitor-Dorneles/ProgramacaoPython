caminho = r"c:\Users\laboratorio\Desktop\ProgramacaoPython\Aulas\Aula_10\listaPalavras.csv"

def ler_lista(caminho_arquivo):
    with open(caminho_arquivo) as arquivo:
        conteudo = arquivo.read()
        lista_palavras_negativas = []
        lista_palavras_negativas = conteudo.splitlines()
        lista_palavras_negativas.sort()
        return lista_palavras_negativas
    
lista_palavras_negativas = ler_lista(caminho)
print(lista_palavras_negativas)
print(len(lista_palavras_negativas))

texto = input('Digite um texto para a analise: ')

lista_texto = []
lista_texto = texto.split()
print(lista_texto)

for palavra_negativa in lista_palavras_negativas:
    ocorrencias = 0
    for palavra_texto in lista_texto:
        if palavra_negativa == palavra_texto:
            ocorrencias += 1

    if ocorrencias > 0:
        print(f'A palavra {palavra_negativa} foi encontrada {ocorrencias} vezes')


# Colocar em decomposição funcional (Funções - Métodos)