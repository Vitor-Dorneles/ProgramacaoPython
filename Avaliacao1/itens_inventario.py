# 4. O Coletor de Itens e Inventário
# Em um jogo de exploração, o jogador tem uma mochila com capacidade máxima de 15kg. Crie um programa que peça o peso de cada item encontrado no cenário, um por um. O while deve permitir a entrada de itens enquanto o peso total não ultrapassar 15kg. Se um item ultrapassar o limite, o programa deve avisar "Mochila cheia, item descartado" e encerrar, mostrando o peso final total.

mochila = 15
peso_mochila = 0
peso_total = 0

while True:
    peso_mochila = float(input("Qual o peso do item encontrado? "))
    peso_total += peso_mochila 
    if peso_total >= mochila:
        break
    
print("Mochila cheia, item descartado")
print("O peso total da mochila de capacidade ",mochila,"kg ficou em ",peso_total)
