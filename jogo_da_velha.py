espacos= ["_","_","_","_","_","_","_","_","_"]
divisoria = "|"
indice = 1
estado_de_jogo = False
valores_jogados = []
jogador = 1
ganhou_x = False
ganhou_o = False
acabou = False
jogadas = 0


def desenhar():
    i = 0
    while i <= 8:
        print(" "*7,espacos[i],divisoria,espacos[i+1],divisoria,espacos[i+2])
        i += 3


print("-"*5,"Jogo da velha","-"*5)
print("Valores para cada local de jogo: ")
for i in range(0,3):
    print(" "*7,indice,divisoria,indice+1,divisoria,indice+2)
    indice += 3
    
while True:
    estado = input("Digite 's' para começar e 'n' para sair: ").lower()
    if estado == "s":
        estado_de_jogo = True
    elif estado == "n":
        break
    else:
        print("Comando inválido")
        continue
    while estado_de_jogo:
        #checar se ja ganhou
        
        
        if acabou:
            espacos= ["_","_","_","_","_","_","_","_","_"]
            valores_jogados = []
            ganhou_x = False
            ganhou_o = False
            acabou = False
            jogador = 1
            jogadas = 0



        for linha in range(0,7,3):
            if espacos[linha] == espacos[linha+1] and espacos[linha] == espacos[linha+2] and (espacos[linha] == "X" or espacos[linha] == "O"):
                if espacos[linha] == "X":
                    ganhou_x = True
                    break
                elif espacos[linha] == "O":
                    ganhou_o = True
                    break
        for coluna in range(0,3):
            if espacos[coluna] == espacos[coluna+3] and espacos[coluna] == espacos[coluna+6] and (espacos[coluna] == "X" or espacos[coluna] == "O"):
                if espacos[coluna] == "X":
                    ganhou_x = True
                    break
                elif espacos[coluna] == "O":
                    ganhou_o = True
                    break
        
        if espacos[0] == espacos[4] and espacos[0] == espacos[8] and (espacos[0] == "X" or espacos[0] == "O"): #diagonal comecando no canto superior esquerdo
            if espacos[0] == "X":
                ganhou_x = True
            elif espacos[0] == "O":
                ganhou_o = True

        if espacos[2] == espacos[4] and espacos[2] == espacos[6] and (espacos[2] == "X" or espacos[2] == "O"): #diagonal comecando no canto superior direito
            if espacos[2] == "X":
                ganhou_x = True
            elif espacos[2] == "O":
                ganhou_o = True

        if ganhou_x:
            desenhar()
            print(f"Parabéns, o jogador 1 (X) ganhou")
            acabou = True
            break
        elif ganhou_o:
            desenhar()
            print(f"Parabéns, o jogador 2 (O) ganhou")
            acabou = True
            break
        if jogadas == 9:
            desenhar()
            print("Deu velha!")
            acabou = True
            break

        #captar as jogadas
        desenhar()
        if jogador == 1:
            jogada_x = input("Jogador 1 (X) insira sua jogada (1-9): ")
            try:
                jogada_x_int = int(jogada_x)
            except ValueError:
                print("Digite um número entre 1 e 9")
            if jogada_x_int <= 0 or jogada_x_int > 9:
                print("Digite um número entre 1 e 9")
                continue
            if jogada_x_int not in valores_jogados:
                valores_jogados.append(jogada_x_int)
                espacos[(jogada_x_int-1)] = "X"
                jogador = 2
                jogadas += 1
                continue
            else:
                print("Jogada já realizada")
        if jogador == 2:
            jogada_o = input("Jogador 2 (O) insira sua jogada (1-9): ")
            try:
                jogada_o_int = int(jogada_o)
            except ValueError:
                print("Digite um número entre 1 e 9")
                continue
            if jogada_o_int <= 0 or jogada_o_int > 9:
                print("Digite um número entre 1 e 9")
                continue
            if jogada_o_int not in valores_jogados:
                valores_jogados.append(jogada_o_int)
                espacos[(jogada_o_int-1)] = "O"
                jogador = 1
                jogadas += 1
            else:
                print("Jogada já realizada")
        