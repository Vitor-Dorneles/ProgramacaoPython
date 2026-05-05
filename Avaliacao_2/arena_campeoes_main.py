from arena_campeoes import *

base = "Avaliacao_2/partida.txt"


jogadores = ler_jogadores(base)

imprimir_relatorio(jogadores)


if len(jogadores) > 0:
    classe = input("\nDigite a classe que você deseja procurar por jogadores: ")
    
    grupo_encontrado = filtrar_por_classe(jogadores, classe)
    
    
    print(f"\n--- Resultado de: '{classe.upper()}' ---")
    if len(grupo_encontrado) > 0:
        for j in grupo_encontrado:
            print(f"- {j['nome']} (Dano: {j['dano']})")
    else:
        print("Nenhum jogador encontrado com esta classe.")