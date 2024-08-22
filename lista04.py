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


