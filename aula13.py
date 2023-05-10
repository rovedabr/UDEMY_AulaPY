nome = "Ivan"
altura = 1.80
peso = 98
imc = peso / (altura)**2
print(imc)

print("Meu nome é " ,nome ,"tenho altura de" ,altura, "e peso de " ,peso, "kgs com IMC de ", imc)

# USANDO LITERAL COM ASPAS E CONCATENAÇÃO DE CASAS DECIMAIS (f-strings)

texto = f'Meu nome é {nome} e tenho altura de {altura}, com peso de {peso}kgs e imc {imc:.2f}.'
print(texto)