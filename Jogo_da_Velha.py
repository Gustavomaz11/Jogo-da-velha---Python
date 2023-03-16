import random
import time
import os

matriz = []
contador_jogador_linha = 0
contador_jogador_coluna = 0
contador_PC_coluna = 0
contador_Pc_linha = 0

def criando_matriz():
    for x in range(3):
        lista = [] 
        for j in range(3):
            lista.append('-')
        matriz.append(lista)

    for i in range(len(matriz)):
        print(matriz[i])
    return matriz


def verifica_vencedor():

    vencedor = False

    for v in range(len(matriz)):
        
        contador_jogador_linha = 0
        contador_jogador_coluna = 0
        contador_PC_coluna = 0
        contador_Pc_linha = 0

        for g in range(len(matriz)):
                
            if matriz[v][g] == "X":
                contador_jogador_linha += 1
                
                if contador_jogador_linha == 3:
                    print("O usuário venceu!")
                    vencedor = True        
                    break
            
            if matriz[v][g] == "O":
                contador_Pc_linha +1
                
                if contador_Pc_linha == 3:
                    print("O computador venceu!")
                    vencedor = True
                    
                    break
            
            if matriz[g][v] == "X":
                contador_jogador_coluna +=1
                if contador_jogador_coluna ==3:
                    print("Usuário Venceu!")
                    vencedor = True
                    break

            if matriz[g][v] == "O":
                contador_PC_coluna += 1
                if contador_PC_coluna == 3:
                    print("Computador Venceu!")
                    vencedor = True
                    break
            
        if matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X":
            print("O usuário venceu!")
            vencedor = True
            break
        
        if matriz[0][2] == "X" and matriz[1][1] =="X" and matriz[2][0] == "X":
            print("O usuário venceu!")
            vencedor = True
            break
        
        if matriz[0][2] == "O" and matriz[1][1] == "O" and matriz[2][0] == "O":
            print("O computador venceu!")
            vencedor = True
            break
        
        if matriz[0][0] == "O" and matriz[1][1] =="O" and matriz[2][2] == "O":
            print("O computador venceu!")
            vencedor = True
            break
    return vencedor
        
def jogo():

    coluna = int(input("Escolha a coluna\n[1]\n[2]\n[3]\nDigite: "))
    linha = int(input("Escolha a linha\n[1]  [2]  [3]\nDigite: "))

    if matriz[linha -1][coluna -1] == "-":
        matriz[linha -1][coluna -1] = "X"

    os.system('cls')
    time.sleep(1)
    print("Vez do computador!")
    time.sleep(2)
    os.system('cls')

    while True:
        
        linha_aleatoria = random.randint(0, 2)
        coluna_aleatoria = random.randint(0, 2)
        
        if matriz[linha_aleatoria][coluna_aleatoria] == "-":
            matriz[linha_aleatoria][coluna_aleatoria] = "O"    
        
            break
    
    time.sleep(2)
    print("Sua Vez!")

    for i in range(len(matriz)):
        print(matriz[i])

criando_matriz()
while True:
    vencedor = verifica_vencedor()
    if vencedor == True:
        break
    jogo()
