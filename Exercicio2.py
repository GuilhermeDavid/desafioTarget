# Função para verificar se um número pertence à sequência de Fibonacci
def pertence_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    if b == num:
        return True
    else:
        return False

def main():
    # Entrada do usuário
    num = int(input("Digite um número: "))

    # Verifica se o número pertence à sequência de Fibonacci
    if pertence_fibonacci(num):
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")
        

if (__name__ == "__main__"):
    main()
