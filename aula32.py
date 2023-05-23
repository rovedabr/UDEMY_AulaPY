# https://docs.python.org/pt-br/3/tutorial/index.html

string = 'Pedro Augusto'
print(string[3])
print(string.zfill(100))

outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(outra_variavel)

string2 = 'pedro Augusto'
print(string2.capitalize())