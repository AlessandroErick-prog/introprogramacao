# Constante

pontos_por_vitoria = 3
pontos_por_empate = 1

# Entrada de dados
print("--- CADASTRO DA SELEÇÃO (COPA DO MUNDO) ---")
selecao = input("Digite o nome da sua seleção: ")
grupo = input("Digite a letra de seu grupo: ")

# Entrada de dados numéricos

vitorias = int(input("Digite a quantidade de vitórias: "))
empates = int(input("Digite a quantidade de empates: "))
derrotas = int(input("Digite a quantidade de derrotas: "))
gols_marcados = int(input("Digite o número de gols marcados: "))
gols_sofridos = int(input("Digite a quantidade de gols sofridos: "))

# Conversão de valores
total_partidas = vitorias + empates + derrotas
total_pontos = (vitorias * pontos_por_vitoria) + pontos_por_empate
saldo_gols = (gols_marcados - gols_sofridos)

# Verificações lógicas

if total_pontos >= 6 and saldo_gols > 0 : 
    status = "classificada"
else:
    status = "eliminada"
    
# Saída organizada

print("\n" + "="*40)
print(f"RESUMO DA SELEÇÃO: {selecao}")
print("="*40)
print(f"Grupo: {grupo}")
print(f"Vitórias: {vitorias}")
print(f"Empates: {empates}") 
print(f"Derrotas: {derrotas}") 
print(f"Total de partidas: {total_partidas}")
print(f"Pontos: {total_pontos}")
print(f"Gols marcados: {gols_marcados}")
print(f"Saldo de gols: {saldo_gols}")
print(f"-"*40)
print(f"Situação: {status}")
print("="*40)

