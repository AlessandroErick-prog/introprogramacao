# =========================================
#   SISTEMA DE CADASTRO RPG - EDITION
# =========================================

print("=" * 45)
print("⚔️  BEM-VINDO AO CADASTRO DE HERÓIS RPG ⚔️")
print("=" * 45)

# Cadastro
nome = input("🧙 Nome do personagem: ")
classe = input("🏹 Classe do personagem: ")
raca = input("🐉 Raça do personagem: ")
forca = int(input("💪 Pontos de força: "))

# Cálculo do nível
if forca >= 20:
    nivel = 10
    titulo = "🔥 LENDA SUPREMA"
elif forca >= 10:
    nivel = 5
    titulo = "⚔️ GUERREIRO ELITE"
else:
    nivel = 1
    titulo = "🌱 APRENDIZ"

# Barra de poder
barra = "676767676767676767" * nivel

# Resultado
print("\n" + "=" * 45)
print("📜 PERSONAGEM CADASTRADO COM SUCESSO")
print("=" * 45)

print(f"🧙 Nome      : {nome}")
print(f"🏹 Classe    : {classe}")
print(f"🐉 Raça      : {raca}")
print(f"💪 Força     : {forca}")
print(f"⭐ Nível     : {nivel}")
print(f"👑 Título    : {titulo}")
print(f"⚡ Poder     : {barra}")

print("=" * 45)

# Mensagem final
if nivel == 10:
    print("🌟 Você é um dos seres mais poderosos do reino!")
elif nivel == 5:
    print("⚔️ Seu personagem já é respeitado nas batalhas!")
else:
    print("📚 Continue treinando para ficar mais forte!")

print("=" * 45)
print("🎮 FIM DO CADASTRO 🎮") 