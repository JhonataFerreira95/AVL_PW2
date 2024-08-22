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