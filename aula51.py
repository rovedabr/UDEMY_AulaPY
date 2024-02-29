number_1 = 0.7
number_2 = 0.1

soma = number_1 + number_2
print(soma)
print(f'{soma:.2f}') #forma 1
print(round(soma, 2)) #forma 2

#Métodos de strings e listas

frase = 'Olha só isso, o que acontece'

#Médoto 1
lista_palavras = frase.split()
print(lista_palavras)

#Médoto 2
lista2_palavras = frase.split(',')
print(lista2_palavras)

#Médoto 3
for i, frase in enumerate(lista_palavras):
  print(lista_palavras[i].strip())

nova_frase = ' - '.join('abcd')
print(nova_frase)

