while True:
    palpite = int(input('Escreva um numero de 1 a 10.000 para verificarmos se ele é primo '))


    if palpite <= 1 or palpite > 10000:
        print('Numero invalido')

    elif palpite == 2 or palpite == 3:
        print('é um numero primo')

    elif palpite % 2 == 0:
        print('nao é primo')
    
   

