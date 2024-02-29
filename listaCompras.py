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
    indice_str = input('Escolha o índice que quer apagar: ')
    try:
      indice = int(indice_str)
      del lista[indice]
      print('Item apagado com sucesso da lista')
    except:
      print('Não foi possível apagar este índice')

  elif opcao == 'l':
    os.system('clear')

    if len('lista') == 0:
      print('Nada para mostrar')

    for i, valor in enumerate(lista):
      print(i, valor)
    else:
     print("Escolha uma das opções descritas (i, a, l)")