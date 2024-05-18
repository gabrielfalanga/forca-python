def exibir_forca(erros):
  'Exibe o desenho da forca de acordo com a quantidade de erros do usuário.'

  print(lista_forcas[erros], end='')


forca_0 = '''\
  ____
 |    |
 |   / \\
 |   \_/
 |
 |
 |
_|_          '''

forca_1 = '''\
  ____
 |   _|_
 |  |___|
 |    |
 |
 |
 |
_|_          '''

forca_2 = '''\
  ____
 |   _|_
 |  |___|
 |    |
 |    |
 |
 |
_|_          '''

forca_3 = '''\
  ____
 |   _|_
 |  |___|
 |   /|
 |  / |
 |
 |
_|_          '''

forca_4 = '''\
  ____
 |   _|_
 |  |___|
 |   /|\\
 |  / | \\
 |
 |
_|_          '''

forca_5 = '''\
  ____
 |   _|_
 |  |___|
 |   /|\\
 |  / | \\
 |   /
 |  /
_|_          '''

forca_final = '''\
  ____
 |   _|_         ______
 |  |X_X|       /      \\
 |   /|\\       | R.I.P. |
 |  / | \\      |        |
 |   / \\      _|________|_
 |  /   \\
_|_          '''


lista_forcas = [forca_0, forca_1, forca_2, forca_3, forca_4, forca_5, forca_final]


# print(forca_0)
# print(forca_1)
# print(forca_2)
# print(forca_3)
# print(forca_4)
# print(forca_5)
# print(forca_final)