nome = input("Digite seu nome: ") #Texto ou String (str

idade = int(input("Digite sua idade: ")) #Numero inteiro

dias = int(input("Quantos dias você deseja ficar no hotel? "))

responasvel = input("Está acompanhado de um responsável? (sim/não): ").lower()

vip = input("Você é cliente VIP? (sim/não)").lower()

aceitou_regras = input("Você aceita as regras do hotel? (sim/não)").lower()

if responavel == "sim":
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