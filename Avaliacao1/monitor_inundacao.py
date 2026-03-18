# 3. Monitor de Inundação (Sentinela)
# Você está desenvolvendo um sistema de alerta para uma Smart City. O programa deve ler o nível do rio (em metros) continuamente.

# * Se o nível for menor que 3m: "Estado Normal".
# * Entre 3m e 5m: "Estado de Alerta".
# * Acima de 5m: "Evacuação Imediata".
# O programa só deve encerrar a leitura se o usuário digitar um valor negativo (flag/bandeira de encerramento).

while True:
    nivel_rio = int(input("Digite o nível do rio atualmente: "))
    
    if nivel_rio < 0:
        break
        
    if nivel_rio > 5:
        print("Evacuação Imediata")
    elif nivel_rio >= 3 and nivel_rio <= 5:
        print("Estado de Alerta")
    elif nivel_rio < 3:
        print("Estado Normal")
        
    print("\nDigite um valor negativo para encerrar o programa\n")

print("Programa encerrado")

