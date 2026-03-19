while True:
    nome_completo = input('Digite seu nome completo: ').strip()
    
    # Transforma o texto em uma lista de palavras
    palavras_nome = nome_completo.split()
    
    # A lista tem pelo menos 2 palavras (nome e sobrenome)?
    if len(palavras_nome) >= 2:
        print(f'\nSeu nome completo é: {nome_completo}')
        print(f'Seu primeiro nome é: {palavras_nome[0]}')
        print(f'Seu sobrenome é: {palavras_nome[-1]}') #Pega o final da lista
        print(f'Seu primeiro nome tem {len(palavras_nome[0])} letras.')
        break
    else:
        print('Nome inválido\n')