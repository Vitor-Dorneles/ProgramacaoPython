#8 - Faça um programa em Python que manipule listas com números inteiros, representando
#    valores de glicemia (45 a 450) de um doente diabético. O programa deve receber valores de 
#    glicemia (um a um) até que o usuário não queira mais cadastrá-los. Os dados digitados
#    devem ser inseridos na lista listaDadosOriginais.
#9 - Faça uma adição/complemento no código anterior para mostrar os valores de glicemia
#    da listaDadosOriginais, um abaixo do outro.
#10 - Faça um complemento no código anterior para copiar a listaDadosOriginais para a 
#     listaDadosOrdenados, que na sequência precisa ser ordenada.
#11 - Faça um complemento no código anterior para mostrar o menor e o maior valores
#     de glicemia cadastrados.
#12 - Faça um complemento no código anterior para mostrar a média dos valores de 
#     glicemia cadastros e na sequência contar e mostrar quantos valores estão abaixo e
#     acima da média.


lista_dados_originais = []
glicemia_usuario = 0
maior_valor_glicemia = 0
menor_valor_glicemia = 450
registro_total = 0
valor_total_glicemia = 0
media_glicemia = 0
valores_abaixo_media = 0
valores_acima_media = 0



while True:
    glicemia_usuario = int(input("Digite seu valor de glicemia atual: "))
    print("Para encerrar o programa digite 1")
    if glicemia_usuario == 1:
        break
    if glicemia_usuario >= 45 and glicemia_usuario <= 450:
        lista_dados_originais.append(glicemia_usuario)
        print("\nValor adicionado na lista de dados")
        registro_total += 1
        valor_total_glicemia += glicemia_usuario
    else:
        print("\nValor de glicemia inválido")
    
media_glicemia = float(valor_total_glicemia/registro_total)    
    
print("Programa encerrado")
print(f"\nLista final com os dados originais:")
for valor in lista_dados_originais:
    print("[",valor,"]")

print("\nValores ordenados do menor ao maior:")
lista_dados_ordenados = lista_dados_originais.copy()
lista_dados_ordenados.sort()
for ordem in lista_dados_ordenados:
    print("[",ordem,"]")
    if maior_valor_glicemia < ordem:
        maior_valor_glicemia = ordem
    if menor_valor_glicemia > ordem:
        menor_valor_glicemia = ordem

print("\nO maior valor de glicemia registrado foi: ", maior_valor_glicemia)
print("O menor valor de glicemia registrado foi: ", menor_valor_glicemia)

for i in lista_dados_ordenados:
    if i < media_glicemia:
        valores_abaixo_media += 1
    if i > media_glicemia:
        valores_acima_media += 1

print(f"\nSua media de glicemia foi:{media_glicemia}")
print(f"Foram registrados {valores_abaixo_media} valores abaixo da média")
print(f"Foram registrados {valores_acima_media} valores acima da média")

