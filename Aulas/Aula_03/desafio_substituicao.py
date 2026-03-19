# Substitua a minúsculo por @
# Substitua e minúsculo por &
frase = input('Digite uma frase: ')

frase_modificada = frase.replace('a', '@').replace('e', '&')

print(f'A frase possui {len(frase)} caracteres')
print(f'A frase original: {frase}')
print(f'A frase em MAIÚSCULO: {frase.upper()}')
print(f'A frase em minúsculo: {frase.lower()}')
print(f'A frase com as substituições: {frase_modificada}')