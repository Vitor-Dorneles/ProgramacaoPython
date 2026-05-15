class jogador:
 
    def __init__(self, nome, idade, sexo, telefone):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.telefone = telefone

def eh_maior_de_idade(self):
    if self.idade >=18:
        return True
    else:
        return False
    
def tem_telefone(self):
    if self.sexo =='Feminino' and self.eh_maior_de_idade():
        return self.telefone
    else:
        return None

# j1 = jogador('gabriel', 21, 'M', 87878)
# j2 = jogador('alisson', 19, 'M', 4545)
# j3 = jogador('Maria', 12, 'F', 4545896 )

# lista_objetos = []
# lista_objetos.append(j1)
# lista_objetos.append(j2)
# lista_objetos.append(j3)

# print(j1.eh_maior_de_idade())

nome_arquivo = 'Aulas\Aula_13_POO\jogadores.csv'

lista_jogadores = []

with open(nome_arquivo, 'r') as arquivo:
    for linha in arquivo:
        nome,idade,sexo, telefone = linha.strip().split(',')
        lista_jogadores.append((nome, int(idade), sexo, telefone))

for jogador in lista_jogadores:
    print(jogador)
    print('-' * 20)

# Criar um método ou uma função ou rotina que insira na lista somente nomes de jogadores não replicados