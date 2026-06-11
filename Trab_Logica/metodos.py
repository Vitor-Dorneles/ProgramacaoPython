from candidato_cad import Candidato_cad

def dados_lista(lista, nome_arquivo):
    leitor = open(nome_arquivo, "r", encoding="utf8")
    next(leitor) #pula a primeira linha

    for linha in leitor:
        vetor_linha = linha.strip().split(",")
        #conversão para boolean
        tem_tecnico = vetor_linha[4].strip() == "Sim" 
        tem_ingles = vetor_linha[5].strip() == "Sim"
        
        obj_candidato = Candidato_cad(
            int(vetor_linha[0]), 
            vetor_linha[1], 
            int(vetor_linha[2]), 
            int(vetor_linha[3]), 
            tem_tecnico, 
            tem_ingles
        )

        if obj_candidato not in lista:
            lista.append(obj_candidato)
    leitor.close()


def exibir_quali_tecnica(candidatos_lista):
    print("\nDesafio 1: Triagem de Qualificação Técnica (Operador E)\n")
    total = 0
    for item in candidatos_lista:
        if item.idade >= 18 and item.tecnico == True:
            print(f"ID: {item.id}\tNome: {item.nome}")
            total += 1
    print(f"Total de candidatos nesta fase: {total}" )


def exibir_talentos_internacionais(candidatos_lista):
    print("\nDesafio 2: Expansão de Talentos Internacionais (Operador OU)\n")
    total = 0
    for item in candidatos_lista:
        if item.exp >= 3 or item.ingles == True:
            print(f"ID: {item.id}\tNome: {item.nome}")
            total += 1
    print(f"Total de candidatos nesta fase: {total}")

def exibir_potencial_jovem(candidatos_lista):
    print("\nDesafio 3: Filtro de Potencial Jovem (Lógica Combinada)\n")
    total = 0
    for item in candidatos_lista:
        if item.idade < 25 and (item.tecnico == True or item.exp >= 1):
            print(f"ID: {item.id}\tNome: {item.nome}")
            total += 1
    print(f"Total de candidatos nesta fase: {total}")

def classificacao_salarial(candidatos_lista):
    print("\nDesafio 4: Classificação Salarial (Operação Condicional)\n")
    junior = []
    senior = []
    for item in candidatos_lista:
        if item.exp > 5:
            senior.append(item.nome)
        else:
            junior.append(item.nome)
    senior.sort()
    junior.sort()
    total = 0
    for nome in senior:
        print(f"Nome: {nome} | Categoria: SÊNIOR")
        total += 1
    print (f"Total de Seniores: {total}\n\n")

    total = 0        
    for nome in junior:
        print(f"Nome: {nome} | Categoria: JÚNIOR")
        total+=1
    print(f"total de juniores: {total}")


