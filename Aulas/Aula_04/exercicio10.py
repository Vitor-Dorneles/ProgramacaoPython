#8 - Faça um programa em Python que manipule listas com números inteiros, representando
#    valores de glicemia (45 a 450) de um doente diabético. O programa deve receber valores de 
#    glicemia (um a um) até que o usuário não queira mais cadastrá-los. Os dados digitados
#    devem ser inseridos na lista listaDadosOriginais.
#9 - Faça uma adição/complemento no código anterior para mostrar os valores de glicemia
#    da listaDadosOriginais, um abaixo do outro.
#10 - Faça um complemento no código anterior para copiar a listaDadosOriginais para a 
#     listaDadosOrdenados, que na sequência precisa ser ordenada.



lista_dados_originais = []
glicemia_usuario = 0



while True:
    glicemia_usuario = int(input("Digite seu valor de glicemia atual: "))
    print("Para encerrar o programa digite 1")
    if glicemia_usuario == 1:
        break
    if glicemia_usuario >= 45 and glicemia_usuario <= 450:
        lista_dados_originais.append(glicemia_usuario)
        print("\nValor adicionado na lista de dados")
    else:
        print("\nValor de glicemia inválido")
    
    
    
print("Programa encerrado")
print(f"\nLista final com os dados originais:")
for valor in lista_dados_originais:
    print("[",valor,"]")

print("\nValores ordenados do menor ao maior:")
lista_dados_ordenados = lista_dados_originais.copy()
lista_dados_ordenados.sort()
for ordem in lista_dados_ordenados:
    print("[",ordem,"]")
