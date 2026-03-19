# 5. Média de Temperatura Global
# Para um painel informativo sobre mudanças climáticas, você precisa calcular a média de temperatura de um período. O usuário deve informar quantos dias deseja analisar. Use o while para ler a temperatura de cada um desses dias. Ao final, o programa deve exibir a média aritmética das temperaturas e informar se a média está "Acima do esperado" (caso seja maior que 25°C) ou "Dentro da normalidade".
dias_analisados = int(input("Informe o quantos dias deseja analisar: "))
dia_atual = 0
dia_contador = 0
dia_total_temperatura = 0
media_temperatura = 0

while True:
    dia_atual = int(input(f"Informe a temperatura do {dia_contador+1}°: "))
    dia_total_temperatura += dia_atual
    dia_contador += 1
    if dia_contador == dias_analisados:
        break

media_temperatura = float(dia_total_temperatura/dias_analisados)

if media_temperatura > 25:
    print("Acima do esperado:  ",media_temperatura)

if media_temperatura <= 25:
    print("Temperatura média dentro da normalidade: ", media_temperatura)