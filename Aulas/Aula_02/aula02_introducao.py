print("OLA")
print("Primeira Aula de programação")

nome= input("Qual é o seu nome?")
idade = int(input("Digite sua idade: "))
sexo = input("Digite seu Sexo [F de feminino ou M de Masculino]:")

if idade >= 18:
  if sexo == "F":
    print("Você é Adulta")
  if sexo == "M":
    print("Você é Adulto")
else:
    print("Você é menor de idade")

anos_dormidos = int(idade / 3)
print(nome, "voce já dormiu", anos_dormidos, "anos")
