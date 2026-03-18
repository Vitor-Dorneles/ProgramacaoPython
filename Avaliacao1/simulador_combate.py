# 2. Simulador de Combate: Turnos de RPG
# Em um jogo de turno, um herói tem 100 de HP e enfrenta um monstro com 100 de HP. O programa deve pedir ao usuário o dano do ataque do herói e o dano do ataque do monstro por rodada. Use um while que continue enquanto ambos estiverem com HP acima de zero. Ao final de cada turno, mostre o HP restante de ambos. Se alguém chegar a 0, encerre e anuncie o vencedor.
vida_heroi = 100
vida_monstro = 100
rodada = 0

while vida_heroi > 0 and vida_monstro > 0:
    rodada += 1
    print("_____Rodada ",rodada,"_____")
    print("O herói inicia atacando")
    valor_ataque_heroi = int(input("Qual o seu dano de ataque?"))
    vida_monstro = vida_monstro - valor_ataque_heroi
    print("Ataque bem sucedido, o monstro ficou com ", vida_monstro, "de HP")
    if vida_monstro <= 0:
        break

    print("\n---VEZ DO MONSTRO---\n")
    valor_ataque_monstro = int(input("Qual o valor de ataque do monstro?"))
    vida_heroi = vida_heroi - valor_ataque_monstro
    print("Ataque do monstro foi bem sucedido, o heroi ficou com ", vida_heroi , "de HP")
    if vida_heroi <= 0:
        break
if vida_heroi > 0:
    print("O herói venceu")
    
if vida_monstro > 0:
    print("O monstro venceu")

    

    


