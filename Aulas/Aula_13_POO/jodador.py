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
    if self.sexo =='F' and self.eh_maior_de_idade():
        return self.telefone
    else:
        return None

j1 = jogador('gabriel', 21, 'M')
j2 = jogador('alisson', 19, 'M')
j3 = jogador('Maria', 12, 'F')

lista_objetos = []
lista_objetos.append(j1)
lista_objetos.append(j2)
lista_objetos.append(j3)

print(j1.eh_maior_de_idade())