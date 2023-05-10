nome = input("Qual o seu nome? ") #? sempre será uma String
print(nome)
print(f'O seu nome é {nome}') #* mostra o valor da variável na frase
print(f'O seu nome é {nome=}') #* mostra o valor da variável na frase

#* CALCULADORA
num1 = input("Entre com o primeiro número: ")
num2 = input("Entre com o segundo número: ")
soma = int(num1) + int(num2)

print(f'A soma dos dois números é: {soma}')