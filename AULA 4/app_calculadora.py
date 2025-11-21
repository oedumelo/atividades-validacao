from calculadora import Calculadora


def executar_calculadora():
    print("=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")


    opcao = input("Escolha uma opcao: ")


    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))


    if opcao == "1":
        print("Resultado:", Calculadora.soma(numero_1, numero_2))
    elif opcao == "2":
        print("Resultado:", Calculadora.subtracao(numero_1, numero_2))
    elif opcao == "3":
        print("Resultado:", Calculadora.multiplicacao(numero_1, numero_2))
    elif opcao == "4":
        print("Resultado:", Calculadora.divisao(numero_1, numero_2))
    else:
        print("Opção inválida!")


if __name__ == "__main__":
    executar_calculadora()
