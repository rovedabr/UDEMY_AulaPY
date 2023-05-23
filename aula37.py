nome = 'Luiz Augusto'
i = 0
novo_nome = ''

while i < len(nome):
    letra = nome[i]
    print(letra)
    novo_nome += f'*{letra}'
    i += 1
novo_nome += '*'

print(novo_nome)