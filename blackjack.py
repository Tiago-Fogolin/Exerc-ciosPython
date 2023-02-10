import random
import time

print("-"*5,"Black Jack","-"*5)
numeros_jogador = []
numeros_bot = []
jogador = 1
soma_jogador = 0
soma_bot = 0
estado_de_jogo = False
resetar = False

def adicionar_numero_jogador():
    x = random.randint(1,13)
    numeros_jogador.append(x)
    return x

def adicionar_numero_bot():
    y = random.randint(1,13)
    numeros_bot.append(y)
    return y

def pontos_jogador():
    print("Seu(s) número(s) são:")
    print(*numeros_jogador, sep=", ")
    print("Soma:", soma_jogador)

def pontos_bot():
    print("O(s) número(s) do bot são:")
    print(*numeros_bot, sep=", ")
    print("Soma do bot:", soma_bot)
while True:
    if resetar:
            numeros_jogador = []
            numeros_bot = []
            jogador = 1
            soma_jogador = 0
            soma_bot = 0
    estado = input("Digite 's' para começar e 'n' para sair: ").lower()
    if estado== "n":
            break
    elif estado == "s":
        estado_de_jogo = True
        soma_jogador += adicionar_numero_jogador()
    else:
        print("Comando inválido")
        continue
    
    while estado_de_jogo:
        pontos_jogador()
        jogada = input("Jogar(1) ou Manter(2)? ").lower()
        
        try:
            jogada_int = int(jogada)
        except:
            print("Digite apenas 1 ou 2")
        
        
        if jogada_int == 1:
            soma_jogador += adicionar_numero_jogador()
        elif jogada_int == 2:
            jogador = 2
        else:
            print("Digite apenas 1 ou 2")
        
        if soma_jogador == 21:
            pontos_jogador()
            print("Você ganhou!")
            resetar = True
            break

        if soma_jogador > 21:
            pontos_jogador()
            print("Você perdeu!")
            resetar = True
            break

        if jogador == 2:
            soma_bot += adicionar_numero_bot()
            while soma_bot <= 17:
                pontos_bot()
                soma_bot += adicionar_numero_bot()
                time.sleep(1)

            if soma_bot > 21:
                pontos_bot()
                print("Você ganhou!")
                resetar = True
                break
            elif soma_bot == 21:
                pontos_bot()
                print("Você perdeu!")
                resetar = True
                break
            elif soma_bot == soma_jogador:
                pontos_bot()
                print("Houve um empate")
                resetar = True
                break
            elif soma_bot > soma_jogador:
                pontos_bot()
                print("Você perdeu!")
                resetar = True
                break
            else:
                pontos_bot()
                print("Você ganhou!")
                resetar = True
                break
    
    
    