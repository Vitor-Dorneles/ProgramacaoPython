#Data: 11/06/2026
#Lucas Bassoto e Vítor Dorneles

from metodos import dados_lista, exibir_quali_tecnica, exibir_talentos_internacionais, exibir_potencial_jovem, classificacao_salarial

candidatos_lista = [] #lista vazia
arquivo = "Trab_Logica/candidatos.csv"
dados_lista(candidatos_lista, arquivo)


exibir_quali_tecnica(candidatos_lista)

exibir_talentos_internacionais(candidatos_lista)

exibir_potencial_jovem(candidatos_lista)

classificacao_salarial(candidatos_lista)