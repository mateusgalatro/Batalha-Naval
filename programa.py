from funcoes import posicao_valida, define_posicoes, preenche_frota 
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
print(frota)