def ler_jogadores(caminho_arquivo):
    jogadores = []
    
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue

                dados = linha.split(";")
                jogador = {
                    "nome":   dados[0],
                    "classe": dados[1],
                    "kills":  int(dados[2]),
                    "deaths": int(dados[3]),
                    "dano":   int(dados[4])
                }

                jogadores.append(jogador)
    except FileNotFoundError:
        print(f"O arquivo '{caminho_arquivo}' não foi encontrado.")
        
    return jogadores


def calcular_kda(kills, deaths):
    if deaths == 0:
        return float(kills)
    return kills / deaths


def maior_dano(jogadores):
    if len(jogadores) == 0:
        return None

    jogador_destaque = jogadores[0]

    for j in jogadores:
        if j["dano"] > jogador_destaque["dano"]:
            jogador_destaque = j  

    return jogador_destaque


def media_kills(jogadores):
    if len(jogadores) == 0:
        return 0.0

    total_kills = 0  

    for j in jogadores:
        total_kills += j["kills"]

    return total_kills / len(jogadores)


def filtrar_por_classe(jogadores, classe):
    jogadores_encontrados = []
    
    for j in jogadores:
        if j["classe"].lower() == classe.lower():
            jogadores_encontrados.append(j)
            
    return jogadores_encontrados


def jogadores_kda_alto(jogadores, minimo=2.0):
    destaques = []
    
    for j in jogadores:
        kda = calcular_kda(j["kills"], j["deaths"])
        
        if kda > minimo:
            destaques.append(j["nome"].upper())
            
    return destaques


def imprimir_relatorio(jogadores):
    if len(jogadores) == 0:
        print("Não temos dados para tirar o relatório.")
        return

    print("----- Arena dos Campeões -----")

    mvp = maior_dano(jogadores)
    print("\nMaior dano causado:")
    print(f"   {mvp['nome']} ({mvp['classe']}) — {mvp['dano']} de dano")

    media = media_kills(jogadores)
    print(f"\nMédia de kills da partida: {media:.2f}")

    destaques = jogadores_kda_alto(jogadores)
    print("\nJogadores com KDA superior a 2.0:")
    for nome in destaques:
        print(f"   - {nome}")

    print("\nJogadores por classe:")
    for classe in ["Guerreiro", "Mago", "Arqueiro", "Ladrão"]:
        grupo = filtrar_por_classe(jogadores, classe)
        nomes = ", ".join(j["nome"] for j in grupo)
        print(f"   {classe}: {nomes}")

    print("\n--------")