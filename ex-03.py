import random
numero_aleatorio = random.randint(1, 5)  
tentativa = 0

while True:

    palpite = int(input('Escreve um numero aleatorio de 1 a 2'))
    tentativa += 1

    if tentativa == numero_aleatorio:
        print('Parabéns! Você acertou em', tentativa, 'tentativa(s). O número aleatório era:', numero_aleatorio)
        break
    else:
        print('Número errado. Tente novamente.')
 


