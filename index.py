# Função para garantir entrada válida de experiência (XP)
def entrada_inteira(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")

# Entrada inicial de dados
nome = input("Digite seu nome de Herói: ")
xp = entrada_inteira("Digite a quantidade de experiência (XP): ")

# Classificação do nível do Herói do Usuário com base na experiência (XP)
if xp < 1000:
    nível = "Ferro"
elif 1001 <= xp <= 2000:
    nível = "Bronze"
elif 2001 <= xp <= 3000:
    nível = "Prata"
elif 5001 <= xp <= 7000:
    nível = "Ouro"
elif 7001 <= xp <= 8000:
    nível = "Platina"
elif 8001 <= xp <= 9000:
    nível = "Ascendente"
elif 9001 <= xp <= 10000:
    nível = "Imortal"
else:
    nível = "Radiante"

# Exibição do resultado
print(f"Uau! {nome}, você está no nível {nível}!")