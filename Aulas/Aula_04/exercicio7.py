#7 - Faça um programa Python que receba duas notas, calcule a média aritmética e mostre o resultado.
#    Além disso, deve mostrar ao lado da média Aprovado (se média >= 7.0) Reprovado (se média <= 3.0),
#    Exame (se média entre 3.0 e 7.0)

nota_1 = float (input("Digite sua primeira nota: "))
nota_2 = float(input("Digite sua segunda nota: "))

media_notas = (nota_1+nota_2)/ 2

if media_notas >= 7:
    print(f"Aprovado, sua média foi: {media_notas}\n")

if media_notas <= 3:
    print(f"Reprovado, sua média foi: {media_notas}\n")

if media_notas < 7 and media_notas > 3:
    print(f"Exame, sua média foi: {media_notas: .2f}")