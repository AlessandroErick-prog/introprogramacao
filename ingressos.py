# Compra de ingressos

nome = input("Digite seu nome: ") #Texto ou String (str)

idade = int(input("Digite sua idade: ")) #Numero inteiro

quantidade = int(input("Quantos ingressos deseja comprar? ")) #Numero inteiro

estudante = input("Você é estudante? (sim/não): ").lower()

aceitou_regras = input("Você aceita os termos da compra? (sim/não): ").lower()

# Conversão para valores
if estudante == "sim":
    tem_estudante = True
else:
    tem_estudante = False

if aceitou_regras == "sim":
    termos = True
else:
    termos = False

# Preço do ingresso
preco = 50

# REGRA 1: Deve aceitar os termos dos ingressos para prosseguir a compra
if not termos:
    print("Compra cancelada!")
    print("Motivo: Você não aceitou os termos da compra.")

# REGRA 2: Menores de 12 anos não podem comprar sozinhos
elif idade < 12:
    print("Compra negada!")
    print("Menores de 12 anos devem estar acompanhados de um responsável.")

else:
    # Cálculo do valor
    total = preco * quantidade

    # REGRA 3: Estudante tem 20% de desconto
    if tem_estudante:
        total = total * 0.8
        print("Desconto de estudante aplicado!")
        print("Compra realizada com sucesso!")

    # REGRA 4: Compra de 5 ou mais ingressos ganha brinde
    if quantidade >= 5:
        print("Parabéns! Você ganhou um brinde!")
        print("Obrigado pela compra!")
    else:
        print("Obrigado pela compra!")
