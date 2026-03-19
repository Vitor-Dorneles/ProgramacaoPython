#4 - O volume de um cubo é determinado através do produto da área da base pela altura, 
#    (mas as arestas do cubo possuem medidas iguais), então temos que:
#    V = Ab * a ou V = a * a * a → V = a³. A partir disso, faça um programa, adequando as variáveis
#    para receber medidas de uma piscina (altura, largura e comprimento), para responder o volume de
#    água necessário para enchê-la.

comprimento_piscina = float(input("Digite o comprimento da piscina (m): "))
altura_piscina = float(input("Digite a altura da piscina (m): "))
largura_piscina = float(input("Digite a largura da piscina (m): "))

volume_piscina = comprimento_piscina * largura_piscina * altura_piscina
litros_agua = volume_piscina * 1000

print(f"Volume da piscina: {volume_piscina:.2f} metros cúbicos")
print(f"Quantidade de água: {litros_agua:.0f} litros")

