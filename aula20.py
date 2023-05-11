# Se qualquer valor for considerado falso a explressão inteira será falsa

#* São considerados Falsy: 0 0.0 '' False - usado também o None

print(True and True )
print(True and True and False)
print(True and True and bool(0))

entrada = input('[E]ntrar [S]air: ')
password = input('Senha: ')

password_permitida = '123456'

if entrada == 'E' and password == password_permitida:
    print("Entrar")
else:
    print("Sair")