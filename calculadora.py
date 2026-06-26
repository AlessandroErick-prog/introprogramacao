# Calculadora simples para VSCode

print("=== CALCULADORA ===")

while True:
    print("\nEscolha uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = input("Digite a opção: ")

    if opcao == "5":
        print("Calculadora encerrada.")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida!")
        continue

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        resultado = num1 + num2
        print("Resultado:", resultado)

    elif opcao == "2":
        resultado = num1 - num2
        print("Resultado:", resultado)

    elif opcao == "3":
        resultado = num1 * num2
        print("Resultado:", resultado)

    elif opcao == "4":
        if num2 == 0:
            print("Erro: divisão por zero!")
        else:
            resultado = num1 / num2
            print("Resultado:", resultado)