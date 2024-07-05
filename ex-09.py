def calcular_serie_harmonica(n):
    soma = 0.0
    for i in range(1, n + 1):
        soma += 1 / i
    return soma

def main():
    while True:
        try:
            n = int(input("Digite um número inteiro positivo (ou 0 para sair): "))
            if n < 0:
                print("Número deve ser positivo. Tente novamente.")
                continue
            elif n == 0:
                print("Programa encerrado.")
                break
            
            resultado = calcular_serie_harmonica(n)
            print(f"A soma da série harmônica até o {n}-ésimo termo é: {resultado:.6f}")
        
        except ValueError:
            print("Entrada inválida. Digite um número inteiro positivo.")
            continue

if __name__ == "__main__":
    main()
