from funcoes import posicao_valida, define_posicoes, preenche_frota, posiciona_frota, monta_tabuleiros, faz_jogada, afundados
frota = {"porta-aviões": [], "navio-tanque": [], "contratorpedeiro": [], "submarino": []}
embarcacoes = {"porta-aviões": [4, 1], "navio-tanque": [3, 2], "contratorpedeiro": [2, 3], "submarino": [1, 4]}
for nome in embarcacoes:
    tamanho = embarcacoes[nome][0]
    quantidade = embarcacoes[nome][1]
    posicionados = 0
    while posicionados < quantidade:
        print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        if tamanho > 1:
            escolha = int(input("[1] Vertical [2] Horizontal >"))
            if escolha == 1:
                orientacao = "vertical"
            else:
                orientacao = "horizontal"
        else:
            orientacao = "vertical"
        if posicao_valida(frota, linha, coluna, orientacao, tamanho):
            frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
            posicionados += 1
        else:
            print("Esta posição não está válida!")

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

total_navios = sum(len(navios) for navios in frota_oponente.values())
posicoes_jogadas = []

jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    jogada_valida = False
    while not jogada_valida:
        linha = int(input("Jogador, qual linha deseja atacar? "))
        while linha < 0 or linha > 9:
            print("Linha inválida!")
            linha = int(input("Jogador, qual linha deseja atacar? "))

        coluna = int(input("Jogador, qual coluna deseja atacar? "))
        while coluna < 0 or coluna > 9:
            print("Coluna inválida!")
            coluna = int(input("Jogador, qual coluna deseja atacar? "))

        if [linha, coluna] in posicoes_jogadas:
            print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
        else:
            jogada_valida = True

    posicoes_jogadas.append([linha, coluna])
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == total_navios:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False