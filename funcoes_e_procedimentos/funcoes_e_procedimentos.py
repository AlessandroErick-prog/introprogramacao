def exibir_boas_vindas():
    print("=" * 30)
    print("  Olá Mundo!")
    print("=" * 30)

exibir_boas_vindas()

print("Fazendo outras coisas no programa...")

exibir_boas_vindas()

print("Mais coisas acontecendo...")

exibir_boas_vindas()


def saudar(nome):
    print(f"Olá, {nome}! Bom te ver por aqui.")

saudar("Ana")
saudar("Carlos")
saudar("Professor")

def exibir_cartao(nome, curso):
    print("-" * 30)
    print(f"Nome : {nome}")
    print(f"Curso: {curso}")
    print("-" * 30)

exibir_cartao("Ana", "Sistemas de Informação")
exibir_cartao("Carlos", "Engenharia")


def somar(a, b):
    resultado = a + b
    return resultado

total = somar(3, 4)
print("A soma é:", total)

def somar_com_print(a, b):
    print(a + b)     

#   - FUNÇÃO: calcula e DEVOLVE um valor (tem retorno).
#   - PROCEDIMENTO: executa uma tarefa, mas NÃO devolve valor (só "faz").

def saudar_com_periodo(nome, saudacao="Bom dia"):
    print(f"{saudacao}, {nome}!")

saudar_com_periodo("Ana")
saudar_com_periodo("Bia", "Boa noite")

#DESAFIO: Criar função que calcula um desconto. 
# A função deve receber 2 parâmetros (preço e o desconto)
#O desconto deve ter valor default de 10%
# A função deve exibir o preço final.

def calcular_desconto(preco, percentual=10):
    return preco - (preco * percentual / 100)

print(calcular_desconto(200))        
print(calcular_desconto(200, 25))  