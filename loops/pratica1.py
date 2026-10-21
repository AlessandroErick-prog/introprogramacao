"""
FOR - FASE 1: Usar o loop for para coletar moedas de ouro 5 vezes.
"""

import random
import time


def fase1_farm():
    print("FASE 1: FARM")
    moedas = 0

    for volta in range(1, 6): 
        moedas_coletadas = random.randint(5, 20)
        moedas += moedas_coletadas 
        print(f"Total coletado: {moedas} moedas de ouro")
        time.sleep(0.3)

    print(f"\nTotal final de moedas: {moedas} moedas de ouro")
    return moedas


"""
FASE 2: BATALHA (WHILE)
A cada turno o jogador vai atacar e o Boss perde HP
"""
def fase2_batalha(moedas):
    print("\nFASE 2: BATALHA")

   
    boss_hp = 100
    jogador_hp = 50
    turno = 1
    bonus_ataque = moedas // 2  
    print(f"O Boss apareceu com {boss_hp} pontos de vida!")
    print(f"Seu bônus de ataque é {bonus_ataque}\n")

    while boss_hp > 0 and jogador_hp > 0:
        print(f"--- Turno: {turno} ---")

       
        dano_jogador = random.randint(8, 15) + bonus_ataque 
        boss_hp -= dano_jogador
        boss_hp = max(boss_hp, 0)
        print(f"Você atacou o Boss causando {dano_jogador} de dano! (HP do boss: {boss_hp})")

        if boss_hp <= 0:
            print("\nO Boss foi derrotado! VITÓRIA!")
            break

       
        dano_boss = random.randint(5, 12)
        jogador_hp -= dano_boss
        jogador_hp = max(jogador_hp, 0)
        print(f"O Boss revidou causando {dano_boss} de dano em você (Seu HP atual: {jogador_hp})")

        if jogador_hp <= 0:
            print("\nVocê foi derrotado...")

        turno += 1
        time.sleep(0.3)

    return jogador_hp > 0


"""
FASE 3: RESTART (DO-WHILE)
"""
def fase3_restart():
    while True:
        print("\nINÍCIO DA PARTIDA")
        moedas = fase1_farm()
        venceu = fase2_batalha(moedas)  

        print("\nFIM DE JOGO!")
        if venceu:
            print("Parabéns, você concluiu o desafio com sucesso")
        else:
            print("Você foi derrotado. Tente novamente!")

        resposta = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if resposta != "s":
            print("Obrigado por jogar!")
            break


if __name__ == "__main__":
    fase3_restart()