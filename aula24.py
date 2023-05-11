# Interpolação de Strings
#*===================================
"""
s - string
d e i - inteiro
f - float
x e X - Hexadecimal
"""
#*===================================

nome = "André"
preco = 1000.857487

variavel = '%s, o preço é de R$ %.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %05X' % (2500, 2500))