prim_valor = input("digite um valor: ")
seg_valor = input("digite outro valor: ")

if prim_valor == seg_valor:
    print("Os dois valores são iguais")
elif prim_valor > seg_valor:
    print(f'O primeiro valor ({prim_valor} é maior que o segundo valor({seg_valor})')
else:
    print(f'O segundo valor ({seg_valor}) é maior que o primeiro valor ({prim_valor})')

    