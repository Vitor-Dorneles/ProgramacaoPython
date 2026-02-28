'''
Receber o nome de um aluno
Receber a nota do aluno no primeiro bimestre
Receber a nota do aluno no segundo bimestre
Receber a nota do aluno no terceiro bimestre
Receber a nota do aluno no quarto bimestre
Calcular a média das notas no bimestre e informar se o aluno está:
  Aprovado (média >= 7)
  Recuperação (média >= 5 e média < 7)
  Reprovado (média < 5)
'''
nota1= float(input("Digite a nota do primeiro bimestre: "))
nota2= float(input("Digite a nota do segundo bimestre: "))
nota3= float(input("Digite a nota do terceiro bimestre: "))
nota4= float(input("Digite a nota do quarto bimestre: "))

media_aluno = float(nota1 + nota2 + nota3 + nota4) / 4

print("A média do aluno é: ", media_aluno)
if media_aluno < 7:
    print("Reprovado")
if media_aluno >= 5 and media_aluno < 7:
      print("Recuperação")
if media_aluno > 5:
     print("Aprovado")