# Sistema de cálculo do IMC

# Constante
LIMITE_IMC = 18.5

# Entrada de dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Variável booleana
maior_de_idade = idade >= 18

# Cálculo do IMC
imc = peso / (altura ** 2)

# Classificação do IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

# Resultado
print("\n===== RESULTADO =====")
print("Nome:", nome)
print("Idade:", idade)
print("Peso:", peso, "kg")
print("Altura:", altura, "m")
print("IMC:", round(imc, 2))
print("Classificação:", classificacao)

# Operador lógico
if maior_de_idade and imc >= LIMITE_IMC:
    print("Você é maior de idade e seu IMC está acima ou dentro do limite mínimo.")
else:
    print("Uma das condições não foi atendida.")

print("=====================")