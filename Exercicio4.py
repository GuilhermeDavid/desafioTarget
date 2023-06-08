def main():

    # Dicionário com os valores de faturamento por estado
    faturamento = {'SP': 67836.43, 'RJ': 36678.66,
                   'MG': 29229.88, 'ES': 27165.48, 'Outros': 19849.53}

    # Soma total dos valores de faturamento
    total = sum(faturamento.values())

    # Cálculo da porcentagem de representação de cada estado
    for estado, valor in faturamento.items():
        porcentagem = (valor / total) * 100
        print(f"{estado} - {porcentagem:.2f}%")


if (__name__ == "__main__"):
    main()
