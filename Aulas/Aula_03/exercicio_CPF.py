while True:
    cpf = input('Digite um CPF (somente números, ou -1 para sair): ').strip()
    
    if cpf == '-1':
        print('Programa encerrado.')
        break
        
    # 2. Validação da regra de negócio
    if len(cpf) == 11 and cpf.isnumeric():
        print('CPF válido!')
        break  
    else:
        print('CPF inválido. Digite 11 números.')