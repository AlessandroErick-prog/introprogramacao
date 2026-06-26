# Sistema de calculo de desconto

print("Sistema de calculo de desconto")

produto = input("Digite o nome do produto: ")

preco = float(input("Digite o preço do produto: "))

#calculo do desconto
#Processamento de dados
desconto = preco * 0.10

preco_final = preco - desconto

# Saída de dados

print("Produto: ",  produto)
print("Desconto: ", desconto)
print("Preço final: ", preco_final)