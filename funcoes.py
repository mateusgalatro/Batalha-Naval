def define_posicoes (linha, coluna, orientacao, tamanho): 
    posicoes = []
    for i in range(tamanho): 
        if orientacao == "vertical": 
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna + i])
    return posicoes


linha = 2
coluna = 4
orientacao = "vertical"
tamanho = 3

