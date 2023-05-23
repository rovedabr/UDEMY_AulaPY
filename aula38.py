""" CALCULADORA USANDO WHILE"""

while True:
    number1 = input("Entre com o primeiro número: ")
    number2 = input("Entre com o segundo número: ")
    operator = input("Entre com um dos operadores (+, -, *, /): ")

    valid_number = None
    operatorsOk = '+-/*'

    number1Float = 0
    number2Float = 0

    try:
        number1Float = float(number1)
        number2Float = float(number2)
        valid_number = True
    except:
        valid_number = None        

    if valid_number is None: 
        print('Um dos números é inválido')
        continue

    if operator not in operatorsOk:
        print('Operador Inválido')
        continue

    if len(operator) > 1:
        print('Digite apenas um operador!')
        continue 

    if operator == "+":
        soma = number1 + number2
        print(f' A soma dos números é {soma}')
    elif operator == "-":
        subtracao = number1 - number2
        print(f' A subtração dos números é {subtracao}')
    elif operator == "*":
        multiplicacao = number1 * number2
        print(f' A multiplicação dos números é {multiplicacao}')
    elif operator == "/":
        divisao = number1 / number2
        print(f' A divisão dos números é {divisao}')
    else:
        print('Fim do código')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair == True:
        break


  