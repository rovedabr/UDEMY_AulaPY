"""
Fatiamento de Strings [i:f:p]
012345678
Olá mundo
-987654321

len = contagem dos carcateres 
"""

variavel = "olá mundo"
print(variavel[2]) #*começa da esquerda para a direita inciiando em 0

print(variavel[-2]) #* começa da direita para a esquerda inciando em -1

print(len(variavel[1]))
print(len(variavel))

print(variavel[0:9:1])
print(variavel[0:9:4])
print(variavel[::-1])