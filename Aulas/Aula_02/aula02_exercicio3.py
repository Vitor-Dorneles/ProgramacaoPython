'''
  Receber o nome de um paciente
  Receber a idade do paciente
  Receber a altura do paciente
  Receber o peso do paciente
  Calcular o IMC = peso / (altura * altura)
  Imprimir o nome, a idade e o IMC do paciente
'''

nome = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade de: "))
altura = float(input("Digite a altura de: "))
peso = float(input("Digite o peso de: "))
imc = int(peso / (altura * altura) )

print("Paciente: ", nome)
print("Idade: ", idade)
print("IMC: ", imc)