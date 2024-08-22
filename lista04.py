# 1. Escreva um programa que leia 10 valores inteiros e armazene em uma lista. O pro-
# grama deve imprimir no terminal quantos valores pares foram digitados pelo usuário.

# Dica: use o operador “%” para verificar se o número é par (ZERO é neutro, ZERO NÃO
# É PAR).

valores = []

for i in range(10):
    valor = int(input("Digite um valor inteiro: "))
    valores.append(valor) 
contador_pares = 0
for i in range(10):
    if valores[i] % 2 == 0 and valores[i] != 0: 
        contador_pares += 1
print(f"Qtd valores par: {contador_pares}")

# 2. Escreva um programa que recebe como entrada valores inteiros para criar duas listas

# de mesmo tamanho. O tamanho das listas deverá ser definido pelo usuário. O pro-
# grama deverá somar os valores pares e ímpar de cada uma das listas. Em seguida,

# comparar as somas e informar qual dos somatórios é maior ou se há um empate.

tamanho = int(input("Digite o tamanho das listas: "))


lista1 = [0] * tamanho
lista2 = [0] * tamanho

print("Digite os valores da primeira lista:")
for i in range(tamanho):
    lista1[i] = int(input())

print("Digite os valores da segunda lista:")
for i in range(tamanho):
    lista2[i] = int(input())

soma_par1 = 0
soma_impar1 = 0
soma_par2 = 0
soma_impar2 = 0

for i in range(tamanho):
    if lista1[i] % 2 == 0 and lista1[i] != 0:
        soma_par1 += lista1[i]
    elif lista1[i] % 2 != 0:
        soma_impar1 += lista1[i]

for i in range(tamanho):
    if lista2[i] % 2 == 0 and lista2[i] != 0:
        soma_par2 += lista2[i]
    elif lista2[i] % 2 != 0:
        soma_impar2 += lista2[i]

print(f"Soma listaPar1: {soma_par1}")
print(f"Soma listaPar2: {soma_par2}")

if soma_par1 < soma_par2:
    print("listaPar1 < listaPar2")
elif soma_par1 > soma_par2:
    print("listaPar1 > listaPar2")
else:
    print("listaPar1 = listaPar2")

print(f"Soma listaImpar1: {soma_impar1}")
print(f"Soma listaImpar2: {soma_impar2}")

if soma_impar1 < soma_impar2:
    print("listaImpar1 < listaImpar2")
elif soma_impar1 > soma_impar2:
    print("listaImpar1 > listaImpar2")
else:
    print("listaImpar1 = listaImpar2")

# 3. leia 10 valores inteiros e armazene em uma lista. O programa deve imprimir no terminal
# quantos valores pares foram digitados pelo usuário. Dica: use o operador “%” para
# verificar se o número é par (ZERO é neutro, ZERO NÃO É PAR).

valores = []

print("Digite 10 valores inteiros:")
for i in range(10):
    valor = int(input())
    valores.append(valor)

contador_pares = 0

for valor in valores:
    if valor % 2 == 0 and valor != 0:
        contador_pares += 1

print(f"Quantidade de valores par: {contador_pares}")

# Questão 04
# tamanho_da_lista = int(input('Digite o valor das listas: '))
# primeira_lista = []
# primeiro_valor_boolean = False
# primeiro_valor_numerico = 0
# elemento_desejado_cert = ['boolean', 'string', 'numero']

tamanho_da_lista = int(input('Digite o valor das listas: '))
primeira_lista = []
elemento_desejado_cert = ['boolean', 'string', 'numero']

for i in range(tamanho_da_lista):
    if i == 0:
        primeiro_valor = input('Digite o primeiro valor string: ')
        primeira_lista.append(primeiro_valor)
    elif i == 1:
        primeiro_valor_boolean = input('Digite o primeiro valor boolean (True/False): ')
        primeira_lista.append(primeiro_valor_boolean.lower() == 'true')
    elif i == 2:
        primeiro_valor_numerico = int(input('Digite o primeiro valor numerico: '))
        primeira_lista.append(primeiro_valor_numerico)
    else:
        elemento_desejado = input('Digite o tipo de elemento desejado (boolean/string/numero): ')
        while elemento_desejado not in elemento_desejado_cert:
            print('Elemento inválido.')
            elemento_desejado = input('Digite outro tipo de elemento desejado: ')
        
        if elemento_desejado == 'boolean':
            outro_valor_boolean = input('Digite outro valor boolean (True/False): ')
            primeira_lista.append(outro_valor_boolean.lower() == 'true')
        elif elemento_desejado == 'string':
            outro_valor_string = input('Digite outro valor string: ')
            primeira_lista.append(outro_valor_string)
        else:
            outro_valor_numerico = int(input('Digite outro valor numerico: '))
            primeira_lista.append(outro_valor_numerico)

print("Lista final:", primeira_lista)

# 5. Escreva um programa que receba como entrada uma sequência de valores inteiros.
# Para tanto, o programa deverá inicialmente solicitar ao usuário quantos valores serão
# fornecidos para análise e só depois solicitar os valores a serem analisados. A análise
# consistirá em identificar e apresentar a partir da sequência de valores fornecidos, o
# menor valor, o maior valor e a média aritmética dos valores.

quantidade = int(input("Digite a quantidade de valores: "))

valores = []
soma = 0

print("Digite os valores:")
for i in range(quantidade):
    valor = int(input())
    valores.append(valor)
    soma += valor 

menor_valor = valores[0]
maior_valor = valores[0]

for i in range(1, quantidade):
    if valores[i] < menor_valor:
        menor_valor = valores[i]
    if valores[i] > maior_valor:
        maior_valor = valores[i]


media = soma / quantidade

print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Média aritmética: {media:.0f}")

# 6. Crie um programa que solicite ao usuário uma lista de números inteiros e uma string
# de mesmo comprimento. O programa deve substituir os números nos índices ímpares
# da lista por caracteres correspondentes da string nos mesmos índices. Exiba a se-
# quência resultante, separada por um espaço em branco.

numeros = input("Digite a lista de números inteiros (separados por espaço): ").split()
string = input("Digite uma string de mesmo comprimento: ")

resultado = []

if len(numeros) != len(string):
    print("A lista de números e a string devem ter o mesmo comprimento.")
else:
    for i in range(len(numeros)):
        if i % 2 == 1:
            resultado.append(string[i])
        else:
            resultado.append(numeros[i])

    print(" ".join(resultado))
