nome = input("Digite seu nome: ") #Texto ou String (str

idade = int(input("Digite sua idade: ")) #Numero inteiro

dias = int(input("Quantos dias você deseja ficar no hotel? "))

responsavel = input("Está acompanhado de um responsável? (sim/não): ").lower()

vip = input("Você é cliente VIP? (sim/não): ").lower()

aceitou_regras = input("Você aceita as regras do hotel? (sim/não)").lower()

if responsavel == "sim":
    tem_responsavel = True
else:
    tem_responsavel = False

if vip == "sim":
    cliente_vip = True
else:
    cliente_vip = False
    
if aceitou_regras == "sim":
    aceitou = True 
else:  
    aceitou = False 
    
# REGRA 1: Concordar com os termos do hotel
# NOT

if not aceitou:
    print("Reserva cancelada.")      
    print("Motivo: Não concordou com as regras")
    
#REGRA 2: Menores de 18 anos precisam do responsável
#AND + NOT
elif idade < 18 and not tem_responsavel:
    print("Reserva negada")
    print("Menores de 18 anos precisam estar acompanhados do responsável")

else:
    print("Reserva confirmada!")
    
#REGRA 3: 3 diárias ou mais OU (OR) VIP = café da manhã

if dias >= 3 or cliente_vip:
    print("Você tem direito ao café da manhã!")
else:
    print("Você não tem direito ao café da manhã!")

#REGRA 4: Cliente que fica 7+ E (AND) são VIPs: quarto melhor

if dias >= 7 and cliente_vip:
    print("Parabéns! Upgrade de quarto liberado!")
else:
    print:("Quarto padrão reservado.")              