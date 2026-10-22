temperatura = []

for i in range(3):
    print(f"\nSemana {i + 1}")
    linha = []
    for j in range(7):
        temp = float(input(f"Digite a temperatura {j + 1}: "))
        linha.append(temp)
    temperatura.append(linha)

print("\n=== BOLETIM DE TEMPERATURAS ===")
for i in range(3):
    media = sum(temperatura[i]) / len(temperatura[i])
    print(f"\nSemana {i + 1}: temperatura média = {media:.2f}°C")