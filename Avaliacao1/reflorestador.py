# 1. O Reflorestador (Loop com Acumulador)
# Em um mini-game de reflorestamento, o jogador deve plantar árvores até atingir uma meta de "Biomassa". Crie um programa que peça ao usuário a meta de biomassa (em unidades). Depois, use um while para ler sucessivamente o valor de biomassa de cada árvore plantada. O programa deve parar assim que a meta for atingida ou superada e exibir quantas árvores foram necessárias.
meta_biomassa= int(input("Digite a sua meta de biomassa (Unidades): "))

valor_total_biomassa = 0
valor_biomassa = 0
arvores = 0

while valor_total_biomassa <= meta_biomassa:
    
    valor_biomassa = int(input("Qual o valor de biomassa da árvore que plantou: "))
    valor_total_biomassa =valor_biomassa + valor_total_biomassa
    arvores += 1
    
print("Foram necessárias", arvores, " arvore(s) para a meta de biomassa de: ",meta_biomassa,", o valor total de biomassa plantada foi: ", valor_total_biomassa )
