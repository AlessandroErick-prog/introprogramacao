import random
import time
 
 
print("-----DESAFIO DE GINÁSIO POKÉMON-----")
print("Bem-vindo ao desafio de ginásio Pokémon!")
 
definir_pokemon = input("Escolha seu Pokémon (Pikachu, Charmander, Bulbasaur): ").lower()
 
if definir_pokemon == "pikachu":
    print("Você escolheu Pikachu! Um Pokémon do tipo Elétrico.")
    print("Seu ataque especial é o 'Choque do Trovão'.")
elif definir_pokemon == "charmander":
    print("Você escolheu Charmander! Um Pokémon do tipo Fogo.")
    print("Seu ataque especial é a 'Lança Chamas'.")
elif definir_pokemon == "bulbasaur":
    print("Você escolheu Bulbasaur! Um Pokémon do tipo Planta.")
    print("Seu ataque especial é o 'Chicote de Vinha'.")
else:
    print("Opção inválida! Por favor, escolha entre Pikachu, Charmander ou Bulbasaur.")
 
def fase_treino():
    print("\nFase de Treino!")
    print("Treine seu Pokémon para aumentar seus pontos de ataque.")
    pontos_ataque = 0
    limite_treino = 2
    for i in range(limite_treino):
        treino = input(f"Treino {i+1}: Digite 'treinar' para aumentar o ataque: ").lower()
        if treino == "treinar":
            pontos_ataque += 10
            print(f"Pontos de ataque aumentados! Total de pontos: {pontos_ataque}")
        else:
            print("Treino não realizado. Tente novamente.")
    return pontos_ataque
 
def fase_batalha():
    print("\nFase de Batalha!")
    print("Prepare-se para a batalha!")
 
fase_batalha()
 
# --- Configuração inicial do jogo ---
hp_treinador = 100
hp_inimigo = 150
 
# Bônus: Aumentar pontos de ataque do Pokémon escolhido
bonus_treino = fase_treino() // 20
if bonus_treino > 0:
    print(f"\nBônus de ataque do Pokémon: {bonus_treino} pontos!")
 
turno = 1
while hp_treinador > 0 and hp_inimigo > 0:
    print(f"\nTurno {turno}:")
    print(f"Seu Pokémon tem {hp_treinador} HP. | O Pokémon inimigo tem {hp_inimigo} HP.")
 
    # Ataque do jogador
    dano_treinador = random.randint(8, 15) + bonus_treino
    hp_inimigo -= dano_treinador
    hp_inimigo = max(hp_inimigo, 0)
    print(f"Você atacou o Pokémon inimigo causando {dano_treinador} de dano! Inimigo: {hp_inimigo} HP")
 
    if hp_inimigo <= 0:
        print("Parabéns! Você derrotou o líder do ginásio!")
        break
 
    # Ataque do líder do ginásio
    dano_inimigo = random.randint(5, 12)
    hp_treinador -= dano_inimigo
    hp_treinador = max(hp_treinador, 0)
    print(f"O líder do ginásio atacou causando {dano_inimigo} de dano! Seu Pokémon agora tem {hp_treinador} HP.")
 
    turno += 1
    time.sleep(0.2)
 
# ----- RESULTADO DA BATALHA -----
if hp_treinador > 0:
    print("\nParabéns! Você venceu a batalha e conquistou a insígnia do ginásio!")
else:
    print("\nInfelizmente, você perdeu a batalha. Tente novamente!")