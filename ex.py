# 11. Escreva um programa que solicite ao usuário o valor das duas dimensões de uma
# matriz. Em seguida, solicite ao usuário e armazene nessa matriz uma quantidade de

# valores inteiros correspondente ao tamanho necessário para preencher todas as posi-
# ções da matriz. O programa deverá exibir a matriz de dimensões “m por n” informar o

# resultado da soma de cada LINHA da matriz.

linhas = int(input("Digite o número de Linhas: "))
colunas = int(input("Digite o número de Colunas: "))

matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite os valores da posição: ({i},{j}): "))
        linha += [valor]
    matriz += [linha]

for i in range(linhas):
    soma_linha = 0
    for j in range(colunas):
        soma_linha += matriz[i][j] 
    print(f"{matriz[i]} = {soma_linha}")

# 12. Escreva um programa que solicite ao usuário o valor das duas dimensões de uma
# matriz. Em seguida, solicite ao usuário e armazene nessa matriz uma quantidade de
# valores inteiros correspondente ao tamanho necessário para preencher todas as posi-
# ções da matriz. O programa deverá exibir a matriz de dimensões “m por n” informar o
# resultado da soma de cada COLUNA da matriz.

m = int(input("Digite o número de linhas (m): "))
n = int(input("Digite o número de colunas (n): "))

matriz = [[0] * n for _ in range(m)]

print(f"Digite {m * n} valores inteiros:")
for i in range(m):
    for j in range(n):
        matriz[i][j] = int(input(f"Digite o valor para a posição [{i + 1}][{j + 1}]: "))
for i in range(m):
    for j in range(n):
        if j == n - 1:
            print(matriz[i][j], end="")
        else:
            print(matriz[i][j], end=" ")
    print()
for j in range(n):
    soma_coluna = 0
    for i in range(m):
        soma_coluna += matriz[i][j]
    print(f"Coluna{j + 1}: {soma_coluna}")

# 13. Escreva um programa que armazene valores inteiros em duas matrizes A e B de tama-
# nho 3x3. Em seguida gere uma terceira matriz C 3x3 formada pelos maiores valores

# de cada posição comparando as duas primeiras matrizes A e B.

linhas = 3
colunas = 3
matriz_a = []
matriz_b = []
matriz_resultante = [[0 for _ in range(linhas)] for _ in range(colunas)]

print("Primeira matriz")
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor das poisições ({i},{j}): "))
        linha += [valor]
    matriz_a += [linha]

print("Segunda matriz")
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor das poisições ({i},{j}): "))
        linha += [valor]
    matriz_b += [linha]

for i in range(colunas):
    for j in range(linhas):
        if matriz_a[i][j] > matriz_b[i][j]:
            matriz_resultante[i][j] = matriz_a[i][j]
        if matriz_a[i][j] < matriz_b[i][j]:
            matriz_resultante[i][j] = matriz_b[i][j]
        else:
            matriz_resultante[i][j] = matriz_a[i][j]
print("Matriz a")
for _ in matriz_a:
    print(_)
print("Matriz b")
for _ in matriz_b:
    print(_)

print("matriz resultante:")

for _ in matriz_resultante:
    print(_)

# 14. Escreva um programa que armazene valores inteiros em uma matrize de tamanho
# 4x4. Em seguida exiba a soma dos elementos que estão em índices de linha ímpar e
# coluna par.

matriz = [[0] * 4 for _ in range(4)]

print("Digite 16 valores inteiros para a matriz 4x4:")
for i in range(4):
    for j in range(4):
        while True:
            entrada = input(f"Digite o valor para a posição [{i + 1}][{j + 1}]: ")
            if entrada.strip() == "":
                print("Por favor, insira um valor inteiro.")
            else:
                try:
                    matriz[i][j] = int(entrada)
                    break
                except ValueError:
                    print("Por favor, insira um valor inteiro válido.")
soma = 0
elementos = []

for i in range(4):
    for j in range(4):
        if i % 2 != 0 and j % 2 == 0:
            soma += matriz[i][j]
            elementos.append(matriz[i][j])
print("Resultado:")
print(" + ".join(map(str, elementos)), "=", soma)


# 15. Escreva um programa que, dada uma matriz de números inteiros aleatórios variando
# entre 100 e 999 de dimensões ‘m’ por ‘n’, ambos podendo variar de 2 a 10, realize os

# seguintes passos: solicite ao usuário as dimensões da matriz; apresente a matriz ge-
# rada de forma aleatória; informe o valor e posição do maior e menor valor na matriz.

import random

matriz = []
linhas = random.randint(2,10)
colunas = random.randint(2,10)

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = random.randint(100,999)
        linha.append(valor)
    matriz.append(linha)

menor_valor = matriz[0][0]
maior_valor = matriz[0][0]
menor_posicao = (0,0)
maior_posicao = (0,0)

for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] < menor_valor:
            menor_valor = matriz[i][j]
            menor_posicao = (i,j)
        if matriz[i][j] > maior_valor:
            maior_valor = matriz [i][j]
            maior_posicao = (i,j)
            
print("Matriz")
for _ in matriz:
    print(_)

print(f"Menor valor: {menor_valor} ({menor_posicao})")
print(f"Maior valor: {maior_valor} ({maior_posicao})")

# 16. Escreva um programa que realiza o produto matricial entre duas matrizes de dimen-
# sões 3x3. Os valores das duas matrizes devem ser gerados de forma aleatória com
# números inteiros aleatórios variando entre 1 e 9. Ao final, apresente as duas matrizes
# geradas de forma aleatória, bem como a matriz resultante do produto.

import random

matriz_A = [[0] * 3 for _ in range(3)]
matriz_B = [[0] * 3 for _ in range(3)]
matriz_resultante = [[0] * 3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        matriz_A[i][j] = random.randint(1, 9)
for i in range(3):
    for j in range(3):
        matriz_B[i][j] = random.randint(1, 9)
for i in range(3):
    for j in range(3):
        for k in range(3):
            matriz_resultante[i][j] += matriz_A[i][k] * matriz_B[k][j]
print("Matriz A:")
for i in range(3):
    for j in range(3):
        if j == 2:
            print(matriz_A[i][j], end="")
        else:
            print(matriz_A[i][j], end=" ")
    print() 
print("Matriz B:")
for i in range(3):
    for j in range(3):
        if j == 2:
            print(matriz_B[i][j], end="")
        else:
            print(matriz_B[i][j], end=" ")
    print()
print("Matriz Resultante:")
for i in range(3):
    for j in range(3):
        if j == 2:
            print(matriz_resultante[i][j], end="")
        else:
            print(matriz_resultante[i][j], end=" ")
    print()

# 17. Escreva um programa que realiza o produto matricial entre duas matrizes de dimen-
# sões ‘j’ por ‘k’ e ‘m’ por ‘n’ fornecidas pelo usuário. Os valores das duas matrizes devem

# ser gerados de forma aleatória com números inteiros aleatórios variando entre dois
# valores, também fornecidos pelo usuário. Ao final, apresente as duas matrizes geradas
# de forma aleatória, bem como a matriz resultante do produto. Caso não seja possível
# realizar o produto matricial, informe a impossibilidade ao usuário e as duas matrizes
# geradas.

import random

linhas_a = int(input("Digite o valor de linhas da primeira matriz: "))
colunas_a = int(input("Digite o valor de colunas da primeira matriz: "))
linhas_b = int(input("Digite o valor de linhas da segunda matriz: "))
colunas_b = int(input("Digite o valor de colunas da seunda matriz: "))

if colunas_a != linhas_b:
    print("Impossibilidade de realizar o produto matricial")
else:

    matriz_a =[]
    matriz_b = []
    matriz_resultante = [[0 for _ in range(colunas_b)] for _ in range(linhas_a)]

    numero_aleatorio_inicial = int(input("Digite o valor do número alatorio inical: "))
    numero_aleatorio_final = int(input("Digite o valor do número alatorio inical: "))

    for i in range (linhas_a):
        linha_a = []
        for j in range(colunas_a):
            valor_a = random.randint(numero_aleatorio_inicial,numero_aleatorio_final)
            linha_a.append(valor_a)
        matriz_a.append(linha_a)

    for i in range (linhas_b):
        linha_b = []
        for j in range(colunas_b):
            valor_b = random.randint(numero_aleatorio_inicial,numero_aleatorio_final)
            linha_b.append(valor_b)
        matriz_b.append(linha_b)

    linhas_a = len(matriz_a)
    colunas_a = len(matriz_a[0])
    linha_b = len(matriz_b)
    colunas_b = len(matriz_b[0])

    for i in range(linhas_a):
        for j in range(colunas_b):
            for k in range(colunas_a):
                matriz_resultante[i][j] += matriz_a[i][k] * matriz_b[k][j]

    for linha in matriz_resultante:
        print(linha)

# 18. Escreva um programa que leia uma matriz de dimensões 3x6 com valores reais. Em
# seguida, o programa deverá imprimir a soma de todos os elementos das colunas ím-
# pares; imprima a média aritmética dos elementos da segunda e quarta colunas; subs-
# titua os valores da sexta coluna pela soma dos valores das colunas 4 e 5; Exiba a
# matriz modificada e a matriz original.

matriz = [[0.0] * 6 for _ in range(3)]

print("Digite 18 valores reais para a matriz 3x6:")
for i in range(3):
    for j in range(6):
        matriz[i][j] = float(input(f"Digite o valor para a posição [{i + 1}][{j + 1}]: "))
soma_colunas_impares = 0.0
soma_coluna_2 = 0.0
soma_coluna_4 = 0.0
soma_coluna_5 = 0.0
for i in range(3):
    for j in range(6):
        if j % 2 != 0:
            soma_colunas_impares += matriz[i][j]
        if j == 1:
            soma_coluna_2 += matriz[i][j]
        if j == 3:
            soma_coluna_4 += matriz[i][j]
        if j == 4:
            soma_coluna_5 += matriz[i][j]
media_colunas_2_4 = (soma_coluna_2 + soma_coluna_4) / 6.0 
for i in range(3):
    matriz[i][5] = matriz[i][3] + matriz[i][4]
print("Soma das colunas ímpares:", soma_colunas_impares)
print("Média aritmética das colunas 2 e 4:", media_colunas_2_4)
print("Matriz Modificada:")
for i in range(3):
    for j in range(6):
        if j == 5:
            print(matriz[i][j], end="")
        else:
            print(matriz[i][j], end=" ")
    print()
print("Matriz Original:")
for i in range(3):
    for j in range(6):
        if j == 5:
            print(matriz[i][j], end="")
        else:
            print(matriz[i][j], end=" ")
    print()