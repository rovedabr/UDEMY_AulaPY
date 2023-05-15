"""
try execpt
"""

number_str = input("Vou dobrar o número que você digitar: ")

try:
    number_float = float(number_str)
    print("FLOAT:", number_float)
    print(f'O dobro do número {number_str} é {number_float * 2}')
    
except:
    print("Isso não é um número")