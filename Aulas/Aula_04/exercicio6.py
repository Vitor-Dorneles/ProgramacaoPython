#6 - Construa um programa em Python em que o usuário insira a sigla de um estado brasileiro em que 
#    uma pessoa nasceu e, em seguida imprima uma das seguintes mensagens: 
#    Carioca Paulista Mineiro Outros estados

estado_sigla = {
    "AC": "Acreano", "AL": "Alagoano", "AP": "Amapaense",
    "AM": "Amazonense", "BA": "Baiano", "CE": "Cearense",
    "DF": "Brasiliense", "ES": "Capixaba", "GO": "Goiano",
    "MA": "Maranhense", "MT": "Mato-grossense", "MS": "Sul-mato-grossense",
    "MG": "Mineiro", "PA": "Paraense", "PB": "Paraibano",
    "PR": "Paranaense", "PE": "Pernambucano", "PI": "Piauiense",
    "RJ": "Carioca", "RN": "Potiguar", "RS": "Gaúcho",
    "RO": "Rondoniense", "RR": "Roraimense", "SC": "Catarinense",
    "SP": "Paulista", "SE": "Sergipano", "TO": "Tocantinense"
}

sigla = input("Digite a sigla do estado em que você nasceu: ").strip().upper()

resultado = estado_sigla.get(sigla, "Sigla inválida. Digite uma sigla válida de um estado brasileiro.")

print(resultado)