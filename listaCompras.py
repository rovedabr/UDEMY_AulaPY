lista = []
import os

while True:
  print('Selecione uma opção')
  opcao = input('[i]nserir [a]pagar [l]istar: ')

  if opcao == 'i':
    os.system('clear')
    valor = input('Valor: ')
    lista.append(valor)
  elif opcao == 'a':
    print('a')
  elif opcao == 'l':
    print('l')
  else:
    print("Escolha uma das opções descritas (i, a, l)")