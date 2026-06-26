# SISTEMA DE MÉDIA DE ALUNOS

# Função para calcular a média

def calcular_media(n1,n2):
    media = (n1 + n2) / 2
    return media

# Função status do aluno

def verificar_status(media):
    if media >= 70:
        return "Aprovado"
    elif media >= 50:    
        return "Recuperação"
    else:
        return "Reprovado"     


# Função Principal

def main():
    print("----- Sistema de calculo da média -----")

    continuar = "s"

    while continuar == "s":
        nome = input("Digite o nome do aluno: ")

        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))

        media = calcular_media(nota1,nota2)

        status = verificar_status(media)

        print("\n------ RESULTADO ------")
        print(f"Aluno: {nome}")
        print(f"Média: {media}")
        print(f"Status: {status}")

        continuar = input("\nDeseja cadastrar outro aluno? (s/n)").lower()

main()        