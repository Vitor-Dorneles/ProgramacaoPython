#8 - Faça um programa em Python que manipule listas com números inteiros, representando
#    valores de glicemia (45 a 450) de um doente diabético. O programa deve receber valores de 
#    glicemia (um a um) até que o usuário não queira mais cadastrá-los. Os dados digitados
#    devem ser inseridos na lista listaDadosOriginais.

lista_dados_originais = []
glicemia_usuario = 0


while True:
    glicemia_usuario = int(input("Digite seu valor de glicemia atual: "))
    print("\n\nPara encerrar o programa digite 1")
    if glicemia_usuario == 1:
        break
    if glicemia_usuario >= 45 and glicemia_usuario <= 450:
        lista_dados_originais.append(glicemia_usuario)
        print("Valor adicionado na lista de dados")
    else:
        print("Valor de glicemia inválido")
    
    
    
print("Programa encerrado")
print(f"Lista final com os dados originais: {lista_dados_originais}")