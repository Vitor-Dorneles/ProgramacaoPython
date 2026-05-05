Analisador de Desempenho: "Arena dos Campeões"

Contexto:
Dado um arquivo .txt que simula o log de uma partida de um jogo de RPG/Combate. Cada linha do arquivo representa as estatísticas finais de um jogador no seguinte formato:

NomeDoJogador; Classe; Kills; Deaths; DanoCausado

Exemplo do arquivo partida.txt

Aragorn;Guerreiro;15;2;4500
Legolas;Arqueiro;22;1;5200
Gandalf;Mago;10;5;8000
Frodo;Ladrão;1;10;500
Gimli;Guerreiro;12;4;3800
Boromir;Guerreiro;8;8;2500
Galadriel;Mago;5;0;9500
Eowyn;Guerreiro;11;3;4100
Faramir;Arqueiro;9;4;3200
Saruman;Mago;18;2;8800
Sauron;Mago;30;1;15000
Gollum;Ladrão;2;15;300
Sam;Ladrão;4;2;1200
Merry;Ladrão;3;4;800
Pippin;Ladrão;2;5;700
Elrond;Mago;7;1;6000
Arwen;Mago;4;0;4500
Theoden;Guerreiro;10;6;3500
Ugluk;Guerreiro;6;12;2000
Lurtz;Arqueiro;14;5;4800

Desafio:
Desenvolver um programa Python que processe esses dados e gere um relatório de performance.

Requisitos do Código:
* Leitura e Tratamento: Criar uma função para ler o arquivo e retornar uma lista de dicionários (AINDA NÃO TRABALHADO EM SALA, MAS ENTRA COMO DESAFÍO), convertendo valores numéricos para int.

Exemplo... o dicionário da linha Aragorn;Guerreiro;15;2;4500 ficaria

{
    "nome": "Aragorn",
    "classe": "Guerreiro",
    "kills": 15,
    "deaths": 2,
    "dano": 4500
}
Continuando o exemplo em código Python ...

# Lista que armazenará todos os dicionários
jogadores = [] 

# Exemplo de processamento dentro do loop de leitura
linha = "Aragorn;Guerreiro;15;2;4500"
dados = linha.strip().split(";")

# Cria o dicionário do jogador atual
jogador = {
    "nome": dados[0],
    "classe": dados[1],
    "kills": int(dados[2]),
    "deaths": int(dados[3]),
    "dano": int(dados[4])
}

# Adiciona o dicionário na lista principal
jogadores.append(jogador)

* Cálculo de KDA: Criar uma função que receba o número de Kills e Deaths e retorne o KDA (Kills divided by Deaths). Dica: Tratar divisão por zero.

* Filtragem por Classe: Criar uma função que receba a lista tratada e o nome de uma classe (ex: "Mago") e retorne apenas os jogadores dessa categoria.

* Destaques da Partida: Identificar e imprimir:
     - O jogador que causou o maior dano.
     - A média de kills da partida.
     - O nome dos jogadores com KDA superior a 2.0, formatados em letras maiúsculas.