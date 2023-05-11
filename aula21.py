entrada = input('[E]ntrar [S]air: ')
password = input('Senha: ')

password_permitida = '123456'

if (entrada == 'E' or entrada == "e") and password == password_permitida:
    print("Entrar")
else:
    print("Sair")


#* o not inverte a expressão