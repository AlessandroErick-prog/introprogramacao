# Função para calcular custos

def calcular_custo(diaria, dias):
    custo = diaria * dias
    return custo

def analisar_viagem(orcamento):
    print("Analisando a viagem")
    if orcamento  >= 8000:
        print("Sua viagem será confortável")
    else:
        print("Sua viagem será econômica")
def exibir_resultados(nome, dias, diaria, lugares):
    print("Resumo da sua viagem")

    print (f"Nome do Viajante: {nome}")
    print(f"Dias de viagem: {dias})")
    print(f"Valor da diária: {diaria}")
    print (f"Locais da viagem: {lugares}")

    custo = calcular_custo(diaria, dias)

    print (f"Gasto total: {custo}")

#PROGRAMA PRINCIPAL
 
print("Bem-vindo ao planejador de viagens")
 
nome = input("Digite o nome do viajante: ")

dias = int(input("Digite o número de dias da viagem: "))

diaria = float(input("Digite o valor da diária: "))

lugares = input("Digite os locais da viagem (separados por vírgula): ").split(",")

orcamento = calcular_custo(diaria, dias)

exibir_resultados(nome, dias, diaria, lugares)

analisar_viagem(orcamento)