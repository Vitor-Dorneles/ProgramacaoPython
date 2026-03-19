# Implementando restrições
invalida_data = True
while(invalida_data):
  invalida_data = False
  data = input('Digite uma data: ')
  dia, mes, ano = data.split('/')
  dia = int(dia)
  mes = int(mes)
  ano = int(ano)

  if(dia < 1 or dia > 31):
      print('Data inválida como dia inválido')
      invalida_data = True
  if (mes < 1 or mes > 12):
      print('Data inválida como mês inválido')
      invalida_data = True
  if (ano < 1900 or ano > 2023):
      print('Data inválida como ano inválido')
      invalida_data = True
  if (invalida_data == False):
    print('Data válida')


