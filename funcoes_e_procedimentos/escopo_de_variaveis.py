# Escopo de variáveis
# Uma variável criada dentro de uma função só existe dentro dela.
# Isso se chama escopo LOCAL. Quando a função termina, ela some.

def testar_escopo():
    mensagem = "Eu só existo dentro da função!"
    print(mensagem)


testar_escopo():

# Já uma variável criada fora de funções é GLOBAL e pode ser LIDA de dentro delas.

taxa = 0.1

def calcular_imposto(valor):
    return valor * taxa

print(calcular_imposto(1000)) 