def main():
    palavra = "Parelelepipedo"
    resultado = ""
    for i in range(len(palavra)-1, -1, -1):
        resultado += palavra[i]
    print(resultado )

if (__name__ == "__main__"):
    main()
