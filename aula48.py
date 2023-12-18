lista = [1,2,3, "A"]
numero = lista[3]
print(numero)
lista[2] = 300
print(lista)
del lista[3]
print(lista)
lista.append(50)
print(lista)
lista.append(70)
print(lista)

lista.pop() #remove o último valor ou o valor do índice indicado
print(lista)

del lista[-1]
print(lista)

lista.insert(0,'teste')
print(lista)

