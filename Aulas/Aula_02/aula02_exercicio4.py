'''
Fazer programa que receba sigla de um estado brasileiro. Contudo, enquanto a sigla digitada não for valida o programa deve solicitar novamente ao usuario.
'''
sigla= str(input("Digite a sigla do estado: "))
lista= ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
while sigla not in lista:
  print("Sigla inválida")
  sigla= str(input("Digite a sigla do estado: "))
print("Sigla válida")