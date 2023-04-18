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
        print("O número {} pertence à sequência de Fibonacci.".format(num))
    else:
        print("O número {} não pertence à sequência de Fibonacci.".format(num))
        

if (__name__ == "__main__"):
    main()