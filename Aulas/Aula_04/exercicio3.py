#3 - Refaça o programa anterior (refatorar) para que o programa recebe a distância e a velocidade média,
#    mas calcule e exiba o tempo da viagem.

distancia_viagem = float(input("Digite a distancia que será percorrida na viagem: "))
velocidade_media = float(input("Digite a velocide media em sua viagem (km/hr): "))

tempo_viagem = float(distancia_viagem / velocidade_media)

print(f"O seu tempo de viagem seguindo essas condições {tempo_viagem: .2f}")
