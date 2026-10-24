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

def preenche_frota (frota, nome_navio, linha, coluna, orientacao, tamanho): 
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota: 
        frota[nome_navio] = []
    frota[nome_navio].append(posicoes)
    return frota  