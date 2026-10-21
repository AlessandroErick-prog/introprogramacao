temperatura = []

for i in range(21):
    print(f"\nDia {i + 1}")
    linha = []
    for j in range(21):
        temp = float(input(f"Digite a temperatura {j + 1}: "))
        linha.append(temp)
    temperatura.append(linha)
