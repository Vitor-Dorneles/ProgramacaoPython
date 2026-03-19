#2 - Faça um programa que ajude motoristas calcular e estimar viagens com diferentes tempos de viagem.
#    O programa deve receber do usuário do sistema (motorista) a distância a ser percorrida e o tempo
#    desejado da viagem. A partir disso, o programa deve calcular e exibir na tela a velocidade média
#    necessária.

distancia_viagem = float(input("Digite a distancia que será percorrida na viagem: "))
tempo_viagem = input("Digite o seu tempo de viagem (hh/mm): ").strip()

partes_tempo = tempo_viagem.split("/")

if len(partes_tempo) != 2:
	print("Formato inválido. Use hh/mm")
else:
	horas = int(partes_tempo[0])
	minutos = int(partes_tempo[1])
	tempo_total_horas = horas + (minutos / 60)

	if tempo_total_horas <= 0:
		print("O tempo da viagem deve ser maior que zero.")
	else:
		velocidade_media = distancia_viagem / tempo_total_horas
		print(f"Velocidade média necessária: {velocidade_media:.2f} km/h")