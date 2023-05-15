"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_entrada = input("Digite um número inteiro: ")

if numero_entrada.isdigit():
    entrada_int = int(numero_entrada)
    resto = int(numero_entrada) % 2

    if resto == 0:
        print("O número é par")
    else:
        print("O número é ímpar")

else:
    print("Você não digitou um número inteiro")




"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
inputHour = input("Digite a hora (formato 24 horas): ")
hour = int(inputHour)

manha = hour >= 0 and hour <= 11
tarde = hour >= 12 and hour <= 17
noite = hour >= 18 and hour <= 23

if manha:
    print("Bom dia!")
if tarde:
    print("Boa tarde!")
if noite:
    print("Boa noite!")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
name = input("Digite o seu nome: ")
nameLenght = (len(name))

if nameLenght <= 4:
    print("Seu nome é curto")
elif nameLenght > 6:
    print("Seu nome é muito grande")
else:
    print("Seu nome é normal")