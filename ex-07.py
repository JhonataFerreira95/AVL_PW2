import math
palpite = int(input('Escreva um numero de 1 a 10.000 para verificarmos se ele é primo '))
raiz = math.sqrt(palpite)

if palpite == 2 or palpite == 3:
    print('é um numero primo')

elif palpite % 2 == 0:
    print('nao é primo')