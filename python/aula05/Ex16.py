

linha_1 = [' ', ' ', ' ']
linha_2 = [' ', ' ', ' ']
linha_3 = [' ', ' ', ' ']
tabuleiro = [linha_1, linha_2, linha_3]

def mostrar_tabuleiro(tabuleiro):
    print("---------------Tabuleiro---------------")
    print("+---+---+---+")
    print("| " + tabuleiro[0][0] + " | " + tabuleiro[0][1] + " | " + tabuleiro[0][2] + " |")
    print("+---+---+---+")
    print("| " + tabuleiro[1][0] + " | " + tabuleiro[1][1] + " | " + tabuleiro[1][2] + " |")
    print("+---+---+---+")
    print("| " + tabuleiro[2][0] + " | " + tabuleiro[2][1] + " | " + tabuleiro[2][2] + " |")
    print("+---+---+---+")


def jogar(tabuleiro, linha, coluna, simbolo):
    tabuleiro[linha][coluna] = simbolo

simbolo_jogador1 = 'X'
simbolo_jogador2 = 'O'
for i in range(0, 6):
    mostrar_tabuleiro(tabuleiro)
    if i % 2 == 0:
        print("Vez do Jogador 1 (X)")
        linha = int(input("Digite a linha (0, 1, 2): "))
        coluna = int(input("Digite a coluna (0, 1, 2): "))
        jogar(tabuleiro, linha, coluna, simbolo_jogador1)
    else:
        print("Vez do Jogador 2 (O)")
        linha = int(input("Digite a linha (0, 1, 2): "))
        coluna = int(input("Digite a coluna (0, 1, 2): "))
        jogar(tabuleiro, linha, coluna, simbolo_jogador2)

mostrar_tabuleiro(tabuleiro)
jogar(tabuleiro, 0, 0, simbolo_jogador1)
mostrar_tabuleiro(tabuleiro)