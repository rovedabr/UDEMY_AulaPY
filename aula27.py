"""
Exercício:
Peça ao usuário para digitar seu nome:
Peça ao usuário para digitar sua idade:
Se o nome e a idade foem digitados, exiba:
  - Seu nome é:
  - Seu nome invertido é:
  - Seu nome contem /não contém espaços
  - Seu nome tem "n" letras
  - A primeira letra de seu nome é
  - A última letra de seu nome é
Se nada for digitado em nome ou idade mostrar a frase:
  "Desculpe, você deixou campos vazios"
"""

name = input("Digite seu nome: ")
age = input("Digite sua idade: ")

if name and age:
    print(f'Seu nome é {name}')
    print(f'Seu nome invertido é {name[::-1]}')

    if " " in name:
        print("Seu nome contém espaço")
    else:
        print("Seu nome não contém espaços")
    
    print(f'Seu nome tem {len(name)} letras')
    print(f'A primeira letra de seu nome é {name[0]}')
    print(f'A última letra de seu nome é {name[-1]}')

else:
    print("Desculpe, você deixou campos vazios")