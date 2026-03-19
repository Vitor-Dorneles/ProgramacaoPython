#// Data: 12/03/2026
# 1 - Um usuário (diabético) de insulina rápida precisa fazer uso do medicamento sempre que for realizar
#    uma refeição. Assim, faça um programa que receba do usuário sua glicemia do momento (mg/dl),
#    meta pré-refeição (em geral é 100 mg/dl), fator de sensibilidade (valor inteiro entre 20 a 60). 
#    A partir desses valores, o programa deve calcular e exibir para o usuário a quantidade de insulina
#    que ele deverá administrar baseada na equação: 
#    quantidade_insulina = (glicemia_do_momento - meta_pre_refeicao) / fator_sensibilidade
glicemia_momento = int(input("Digite sua glicemia do momento (mg/dl): "))
meta_pre_refeicao = int(input("Digite sua meta antes da sua refeição: "))
fator_sensibilidade = int(input("Digite o seu fator de sensibilidade: "))

if not 20 <= fator_sensibilidade <= 60:
    print("Fator de sensibilidade inválido (informe um valor entre 20 e 60).")
else:
    quantidade_insulina = (glicemia_momento - meta_pre_refeicao) / fator_sensibilidade

    if quantidade_insulina <= 0:
        print("\nNão é necessária a aplicação")
    else:
        print(f"Deve aplicar {quantidade_insulina:.2f} unidades de insulina")
