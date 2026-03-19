while (True):
  nome_completo = input('Digite seu nome completo: ')
  palavras_nome = nome_completo.split()
  if (len(palavras_nome) >= 2):
    primeiro = palavras_nome[0].lower()
    sobrenome = palavras_nome[-1].lower()
    email = primeiro + '.' + sobrenome + '@ufn.edu.br'
    print('Seu email criado é: ',email)
    break

  print('Nome inválido')
