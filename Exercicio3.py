import statistics


def main():

        # Exemplo de dados de faturamento diário
    faturamento = [1000, 1500, 800, 1200, 0, 0, 2000, 1800, 900, 1100, 1400, 1700,
                        0, 0, 1300, 900, 1100, 1400, 1800, 2000, 0, 0, 1200, 1500, 1000, 900, 800, 1100]

    # Calcular o menor e o maior valor de faturamento
    menor = min(faturamento)
    maior = max(faturamento)

    # Calcular a média mensal de faturamento, ignorando dias sem faturamento
    faturamento_sem_zeros = [f for f in faturamento if f > 0]
    media_mensal = statistics.mean(faturamento_sem_zeros)

    # Contar o número de dias em que o valor de faturamento foi superior à média mensal
    acimaMedia = len([f for f in faturamento if f > media_mensal])

    # Imprimir os resultados
    print(f"Menor faturamento: R$ {menor:.2f}")
    print(f"Maior faturamento: R$ {maior:.2f}")
    print(f"Número de dias com faturamento acima da média: {acimaMedia}")
    
if (__name__ == "__main__"):
    main()

