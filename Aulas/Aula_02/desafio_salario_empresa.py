# Fazer em casa

# receber o nome de um funcionario, valor da hora de trabalho, qnt de horas,e ano de ingresso
# calcular salario = valor da base * horas trabalhadas por semana
# contudo, se estiver entre 4 e 8 anos, adicionar 4% ao salario
# se estiver entre 8 e 12 anos, adicionar 6% ao salario
# se estiver entre 12 e 16 anos, adicionar 8% ao salario
# exibir nome e salario


nome_funcionario = (input("Digite seu nome: "))
hora_trabalho = float(input("Digite o valor de sua hora trabalhada: "))
quantidade_horas = (input("Quantidade de horas semanais trabalhadas (hh:mm): "))

horas, minutos = quantidade_horas.split(':')
minutos = int(minutos)
horas = int(horas)
tempo_decimal = horas + (minutos/60)

salario_funcionario = (hora_trabalho * tempo_decimal)
salario_final = salario_funcionario

ano_ingresso = int(input("Digite o ano que iniciou na empresa: "))
anos_na_empresa = int(2026 - ano_ingresso)
if anos_na_empresa >= 4 and anos_na_empresa < 8:
    salario_final = salario_funcionario * 1.04

if anos_na_empresa >= 8 and anos_na_empresa < 12:
    salario_final = salario_funcionario * 1.06

if anos_na_empresa >= 12 and anos_na_empresa < 16:
    salario_final = salario_funcionario * 1.08

salario_final = salario_final*4 #representando 4 semanadas
print(f"\nO funcionario {nome_funcionario} tem direito a receber  mensal R${salario_final: .2f}, estando a {anos_na_empresa} anos na empresa")
