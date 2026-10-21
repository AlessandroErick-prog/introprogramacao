# === JORNADA DO HERÓI ===
nome_heroi = ""
classe_heroi = ""
hp_heroi = 0
ataque_heroi = 0
defesa_heroi = 0
mana_heroi = 0
ouro_heroi = 0
pocoes_heroi = 0

def criar_personagem():
    global nome_heroi, classe_heroi, hp_heroi, ataque_heroi, defesa_heroi, mana_heroi
    print("=== JORNADA DO HERÓI ===")
    nome_heroi = input("Nome do herói: ")
    print("1-Guerreiro 2-Mago 3-Arqueiro 4-Ladino")
    classe = input("Escolha a classe do herói (1, 2, 3 ou 4): ")
    
    match classe:
        case "1":
            classe_heroi, hp_heroi, ataque_heroi, defesa_heroi, mana_heroi = "Guerreiro", 120, 18, 12, 0
        case "2":
            classe_heroi, hp_heroi, ataque_heroi, defesa_heroi, mana_heroi = "Mago", 80, 22, 4, 50
        case "3":
            classe_heroi, hp_heroi, ataque_heroi, defesa_heroi, mana_heroi = "Arqueiro", 100, 20, 8, 10
        case "4":
            classe_heroi, hp_heroi, ataque_heroi, defesa_heroi, mana_heroi = "Ladino", 90, 16, 6, 20
        case _:
            print("Escolha inválida! Criando herói padrão (Guerreiro).")
            classe_heroi, hp_heroi, ataque_heroi, defesa_heroi, mana_heroi = "Guerreiro", 120, 18, 12, 0

def ver_ficha():
    print("=== FICHA ===")
    print("Nome:", nome_heroi)
    print("Classe:", classe_heroi)
    print("HP:", hp_heroi)
    print("Ataque:", ataque_heroi)
    print("Defesa:", defesa_heroi)
    print("Mana:", mana_heroi)
    print("Ouro:", ouro_heroi)
    print("Poções:", pocoes_heroi)

def batalha():
    global hp_heroi, ouro_heroi, pocoes_heroi
    
    print("=== BATALHA ===")
    print("1-Lobo 2-Goblin 3-Troll")
    monstro = input("Escolha o monstro (1, 2 ou 3): ")
    
    match monstro:
        case "1":
            nome_m, hp_m, ataque_m, ouro_m = "Lobo", 40, 10, 15
        case "2":
            nome_m, hp_m, ataque_m, ouro_m = "Goblin", 60, 14, 25
        case "3":
            nome_m, hp_m, ataque_m, ouro_m = "Troll", 110, 20, 50
            
    while hp_m > 0 and hp_heroi > 0:
        print(f"Você: {hp_heroi} HP | {nome_m}: {hp_m} HP")
        print("1-Atacar 2-Poção")
        escolha = input("Escolha: ")
        
        match escolha:
            case "1":
                hp_m = hp_m - ataque_heroi
                print("Você causou", ataque_heroi, "de dano!")
            case "2":
                if pocoes_heroi > 0:
                    hp_heroi = hp_heroi + 30
                    pocoes_heroi = pocoes_heroi - 1
                    print("Você usou uma poção e recuperou 30 de HP!")
                else:
                    print("Você não tem poções!")
                    continue
            case _:
                print("Escolha inválida!")
                continue
                
        # Turno do monstro (só acontece se ele ainda estiver vivo)
        if hp_m > 0:
            # Bônus: A defesa do herói agora reduz o dano recebido (mínimo 1 de dano)
            dano_recebido = max(1, ataque_m - defesa_heroi)
            hp_heroi = hp_heroi - dano_recebido
            print(f"O {nome_m} causou {dano_recebido} de dano (Sua defesa bloqueou {defesa_heroi}!).")
            
    if hp_heroi > 0:
        print("Você derrotou o", nome_m + "!")
        ouro_heroi = ouro_heroi + ouro_m
        print("Você ganhou", ouro_m, "de ouro!")
    else:
        print("Você perdeu! Fim de jogo.")

def loja():
    global ouro_heroi, pocoes_heroi, defesa_heroi
    while True:
        print("=== LOJA === Ouro:", ouro_heroi)
        print("1-Poção(20) 2-Defesa+5(40) 3-Sair")
        escolha = input("Escolha: ")
        match escolha:
            case "1":
                if ouro_heroi >= 20:
                    ouro_heroi -= 20
                    pocoes_heroi += 1
                    print("Você comprou uma poção!")
                else:
                    print("Ouro insuficiente!")
            case "2":
                if ouro_heroi >= 40:
                    ouro_heroi -= 40
                    defesa_heroi += 5
                    print("Sua defesa aumentou!")
                else:
                    print("Ouro insuficiente!")
            case "3":
                print("Até a próxima, " + nome_heroi + "!")
                break
            case _:
                print("Escolha inválida!")

def menu():
    while True:
        print("=== MENU ===")
        print("1-Ficha 2-Batalhar 3-Loja 4-Sair")
        escolha = input("Escolha: ")
        match escolha:
            case "1":
                ver_ficha()
            case "2":
                batalha()
            case "3":
                loja()
            case "4":
                print("Até a próxima,", nome_heroi + "!")
                break
            case _:
                print("Escolha inválida!")

# Início do Jogo
criar_personagem()
menu()