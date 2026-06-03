NOME_MISSAO = "Missao Prime"
NOME_EQUIPE = "Projeto Aurora"

dados_missao = [
    [22, 95, 91, 97, 93],
    [25, 88, 79, 95, 88],
    [33, 70, 52, 92, 72],
    [38, 55, 21, 88, 58],
    [41, 38, 11, 84, 40],
    [35, 62, 34, 86, 55],
    [28, 78, 48, 90, 68],
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicacao com a base",
    "Sistema de energia",
    "Suporte de oxigenio",
    "Estabilidade operacional",
]


def analisar_temperatura(temp):
    if temp < 18:
        return ("ATENCAO", 1, "Temperatura baixa")
    elif temp <= 30:
        return ("NORMAL", 0, "Temperatura estavel")
    elif temp <= 35:
        return ("ATENCAO", 1, "Temperatura elevada")
    else:
        return ("CRITICO", 2, "Risco de superaquecimento")


def analisar_comunicacao(com):
    if com < 30:
        return ("CRITICO", 2, "Comunicacao com a base em nivel critico")
    elif com < 60:
        return ("ATENCAO", 1, "Comunicacao instavel")
    else:
        return ("NORMAL", 0, "Comunicacao estavel")


def analisar_bateria(bat):
    if bat < 20:
        return ("CRITICO", 2, "Bateria em nivel critico")
    elif bat < 50:
        return ("ATENCAO", 1, "Bateria abaixo do recomendado")
    else:
        return ("NORMAL", 0, "Energia estavel")


def analisar_oxigenio(oxi):
    if oxi < 80:
        return ("CRITICO", 2, "Oxigenio em nivel critico")
    elif oxi < 90:
        return ("ATENCAO", 1, "Oxigenio abaixo do ideal")
    else:
        return ("NORMAL", 0, "Oxigenio adequado")


def analisar_estabilidade(est):
    if est < 40:
        return ("CRITICO", 2, "Estabilidade operacional critica")
    elif est < 70:
        return ("ATENCAO", 1, "Estabilidade operacional reduzida")
    else:
        return ("NORMAL", 0, "Estabilidade operacional adequada")


def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSAO ESTAVEL"
    elif pontuacao <= 5:
        return "MISSAO EM ATENCAO"
    else:
        return "MISSAO CRITICA"


def gerar_recomendacao(resultados):
    acoes = [
        "verificar controle termico da missao",
        "tentar restabelecer contato com a base",
        "ativar modo de economia de energia",
        "acionar protocolo de suporte a vida",
        "reduzir operacoes nao essenciais",
    ]

    criticos = []
    for i in range(len(resultados)):
        classificacao = resultados[i][0]
        if classificacao == "CRITICO":
            criticos.append(acoes[i])

    if len(criticos) >= 3:
        return "Ativar modo de seguranca e priorizar suporte a vida, energia e comunicacao."
    elif len(criticos) > 0:
        return "Acao urgente: " + criticos[0].capitalize() + "."
    else:
        return "Manter operacao normal e continuar monitoramento."


def analisar_tendencia(lista_pontuacoes):
    primeiro = lista_pontuacoes[0]
    ultimo = lista_pontuacoes[-1]

    if ultimo > primeiro:
        return "A missao apresentou tendencia de piora."
    elif ultimo < primeiro:
        return "A missao apresentou tendencia de melhora."
    else:
        return "A missao permaneceu estavel em relacao ao inicio."


def identificar_area_mais_afetada(dados):
    pontuacao_areas = [0, 0, 0, 0, 0]

    for ciclo in dados:
        temp = ciclo[0]
        com = ciclo[1]
        bat = ciclo[2]
        oxi = ciclo[3]
        est = ciclo[4]

        pontuacao_areas[0] = pontuacao_areas[0] + analisar_temperatura(temp)[1]
        pontuacao_areas[1] = pontuacao_areas[1] + analisar_comunicacao(com)[1]
        pontuacao_areas[2] = pontuacao_areas[2] + analisar_bateria(bat)[1]
        pontuacao_areas[3] = pontuacao_areas[3] + analisar_oxigenio(oxi)[1]
        pontuacao_areas[4] = pontuacao_areas[4] + analisar_estabilidade(est)[1]

    maior = pontuacao_areas[0]
    indice = 0
    for i in range(1, len(pontuacao_areas)):
        if pontuacao_areas[i] > maior:
            maior = pontuacao_areas[i]
            indice = i

    return areas_monitoradas[indice], pontuacao_areas


def processar_missao(dados):
    lista_pontuacoes = []

    print("=" * 60)
    print("MISSION CONTROL AI")
    print("=" * 60)
    print("Missao: " + NOME_MISSAO)
    print("Equipe: " + NOME_EQUIPE)
    print("Quantidade de ciclos analisados: " + str(len(dados)))
    print("=" * 60)

    for numero in range(len(dados)):
        ciclo = dados[numero]

        temp = ciclo[0]
        com = ciclo[1]
        bat = ciclo[2]
        oxi = ciclo[3]
        est = ciclo[4]

        r_temp = analisar_temperatura(temp)
        r_com = analisar_comunicacao(com)
        r_bat = analisar_bateria(bat)
        r_oxi = analisar_oxigenio(oxi)
        r_est = analisar_estabilidade(est)

        pontuacao = r_temp[1] + r_com[1] + r_bat[1] + r_oxi[1] + r_est[1]
        lista_pontuacoes.append(pontuacao)

        classificacao = classificar_ciclo(pontuacao)
        recomendacao = gerar_recomendacao([r_temp, r_com, r_bat, r_oxi, r_est])

        print("\nCICLO " + str(numero + 1))
        print("-" * 60)
        print("Temperatura:  " + str(temp) + " C  | " + r_temp[0] + " | " + r_temp[2])
        print("Comunicacao:  " + str(com) + "%   | " + r_com[0] + "  | " + r_com[2])
        print("Bateria:      " + str(bat) + "%   | " + r_bat[0] + "  | " + r_bat[2])
        print("Oxigenio:     " + str(oxi) + "%   | " + r_oxi[0] + "  | " + r_oxi[2])
        print("Estabilidade: " + str(est) + "%   | " + r_est[0] + "  | " + r_est[2])
        print("\nPontuacao de risco do ciclo: " + str(pontuacao))
        print("Classificacao do ciclo: " + classificacao)
        print("Recomendacao: " + recomendacao)

    return lista_pontuacoes


def gerar_relatorio_final(dados, lista_pontuacoes):
    n = len(dados)

    soma_temp = 0
    soma_com = 0
    soma_bat = 0
    soma_oxi = 0
    soma_est = 0

    for ciclo in dados:
        soma_temp = soma_temp + ciclo[0]
        soma_com = soma_com + ciclo[1]
        soma_bat = soma_bat + ciclo[2]
        soma_oxi = soma_oxi + ciclo[3]
        soma_est = soma_est + ciclo[4]

    media_temp = soma_temp / n
    media_com = soma_com / n
    media_bat = soma_bat / n
    media_oxi = soma_oxi / n
    media_est = soma_est / n

    maior_risco = lista_pontuacoes[0]
    ciclo_critico = 1
    for i in range(1, len(lista_pontuacoes)):
        if lista_pontuacoes[i] > maior_risco:
            maior_risco = lista_pontuacoes[i]
            ciclo_critico = i + 1

    soma_risco = 0
    for p in lista_pontuacoes:
        soma_risco = soma_risco + p
    risco_medio = soma_risco / n

    qtd_criticos = 0
    for p in lista_pontuacoes:
        if p >= 6:
            qtd_criticos = qtd_criticos + 1

    tendencia = analisar_tendencia(lista_pontuacoes)
    area_afetada, pontos_areas = identificar_area_mais_afetada(dados)
    classif_final = classificar_ciclo(round(risco_medio))

    print("\n" + "=" * 60)
    print("RELATORIO FINAL DA MISSAO")
    print("=" * 60)
    print("Missao: " + NOME_MISSAO)
    print("Equipe: " + NOME_EQUIPE)
    print("\nQuantidade de ciclos analisados: " + str(n))
    print("\nMedias dos sensores:")
    print("  Temperatura:  " + str(round(media_temp, 2)) + " C")
    print("  Comunicacao:  " + str(round(media_com, 2)) + "%")
    print("  Bateria:      " + str(round(media_bat, 2)) + "%")
    print("  Oxigenio:     " + str(round(media_oxi, 2)) + "%")
    print("  Estabilidade: " + str(round(media_est, 2)) + "%")
    print("\nCiclo mais critico: Ciclo " + str(ciclo_critico))
    print("Maior pontuacao de risco: " + str(maior_risco))
    print("Risco medio da missao: " + str(round(risco_medio, 2)))
    print("Quantidade de ciclos criticos: " + str(qtd_criticos))
    print("\nTendencia da missao:")
    print(tendencia)
    print("\nPontuacao acumulada por area:")
    for i in range(len(areas_monitoradas)):
        print("  " + areas_monitoradas[i] + ": " + str(pontos_areas[i]) + " pontos")
    print("\nArea mais afetada:")
    print(area_afetada)
    print("\nClassificacao final da missao:")
    print(classif_final)


lista_pontuacoes = processar_missao(dados_missao)
gerar_relatorio_final(dados_missao, lista_pontuacoes)