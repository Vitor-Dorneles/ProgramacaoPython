import requests

class CidadeClima:

    def __init__(self, nome, temperatura, umidade, condicao):
        self.nome        = nome
        self.temperatura = temperatura
        self.umidade     = umidade
        self.condicao    = condicao

    def __str__(self):
        return (
            f"  Cidade     : {self.nome}\n"
            f"  Temperatura: {self.temperatura}°C\n"
            f"  Umidade    : {self.umidade}%\n"
            f"  Condição   : {self.condicao}\n"
        )

def buscar_clima(cidade):

    api= f"https://wttr.in/{cidade}?format=j1" # formato json

    resposta = requests.get(api, timeout=10)

    dados = resposta.json()  # dicionario

    temperatura = dados["current_condition"][0]["temp_C"]  
    umidade     = dados["current_condition"][0]["humidity"]
    condicao    = dados["current_condition"][0]["weatherDesc"][0]["value"]

    return CidadeClima(cidade, temperatura, umidade, condicao)



cidades = ["Santa Maria", "Caçapava do Sul", "Porto Alegre", "Pelotas"]

relatorio_clima = []  # lista vazia que vai receber os objetos

print("Buscando dados de clima\n")

for cidade in cidades:
    objeto = buscar_clima(cidade)
    relatorio_clima.append(objeto)

print("-" * 20)             
print("       Tempo Hoje")
for cidade in relatorio_clima:  
    print(cidade)               
    print("=" * 20)             