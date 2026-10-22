notas = []

for i in range(3):
    print(f"\nAluno (i + 1)")
    linha = []
    for j in range(3):
        nota = float(input(f"Digite a nota {j + 1}: "))
        linha.append(nota)
    notas.append(linha)

print("\n=== BOLETIM DE NOTAS ===")
for i in range(3):
    media = sum(notas[i]) / len(notas[i])
    print(f"\nAluno {i + 1}: media final = {media:.2f}")