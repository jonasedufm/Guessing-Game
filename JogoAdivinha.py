import random  # Importa o módulo random para gerar números aleatórios

def JogoAdivinha():  # Define a função principal do jogo
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Estou pensando em um número entre 1 e 100. Tente adivinhar!")

    numero_secreto = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
    tentativas = 0  # Inicia o contador de tentativas

    while True:  # Inicia o loop principal do jogo
        palpite = int(input("Digite seu palpite: "))  # Obtém o palpite do jogador
        tentativas += 1  # Incrementa o contador de tentativas

        if palpite < numero_secreto:
            print("Tente um número maior.")  # Fornece uma dica se o palpite for baixo
        elif palpite > numero_secreto:
            print("Tente um número menor.")  # Fornece uma dica se o palpite for alto
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            break  # Sai do loop se o jogador acertar o número

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
    JogoAdivinha()  # Chama a função principal do jogo
