#----------------------       Desafio BrasilPrev   ---------------------------

import random
from collections import Counter

"""Definindo as caracteristicas dos jogadores"""

jogadores = {
    "jogador_01":
    {
        "status": "ativo",
        "dinheiro": 300,
        "personalidade": "impulsivo",
        "vitorias": 0,
        "casa_atual": 0
    },
    "jogador_02":
    {
        "status": "ativo",
        "dinheiro": 300,
        "personalidade": "exigente",
        "vitorias": 0,
        "casa_atual": 0
    },
    "jogador_03":
    {
        "status": "ativo",
        "dinheiro": 300,
        "personalidade": "cauteloso",
        "vitorias": 0,
        "casa_atual": 0
    },
    "jogador_04":
    {
        "status": "ativo",
        "dinheiro": 300,
        "personalidade": "aleatorio",
        "vitorias": 0,
        "casa_atual": 0
    }
}

""" Criando as propriedades utilizando loop para economizar linhas"""

propriedades = {}

for i in range(1, 21):
    if (i%2) == 0:
        propriedades[i] = {"dono": None, "valor": 100, "aluguel": 40}
    if (i%2) == 1:
        propriedades[i] = {"dono": None, "valor": 120, "aluguel": 55}

#Setando a ordem de jogo

ordem_de_jogo = ["jogador_01", "jogador_02", "jogador_03", "jogador_04"]
random.shuffle(ordem_de_jogo)

turno = []

""" Criando funções para cada jogador"""

"""----------------------------------  jogador 01  ----------------------------------------"""
def jogador_01():
    #Gira o dado e seta o valor da casa atual
    dado = random.randint(1, 6)
    casa_atual = jogadores["jogador_01"].get('casa_atual') + dado

    #Condicional para impedir que a casa_atual passe de 20 e adiciona dinheiro a cada volta no tabuleiro
    if casa_atual > 20:
        casa_atual -= 20
        dinheiro = jogadores["jogador_01"].get('dinheiro')
        jogadores["jogador_01"]['casa_atual'] = casa_atual
        jogadores["jogador_01"]['dinheiro'] = dinheiro + 100
    else:
        jogadores["jogador_01"]['casa_atual'] = casa_atual

    #Checa a possibilidade de compra de acordo com sua personalidade
    if propriedades[casa_atual]['dono'] == None and jogadores["jogador_01"]['dinheiro'] >= propriedades[casa_atual]['valor']:

        #Faz a compra da propriedade
        propriedades[casa_atual]['dono'] = 'jogador_01'
        jogadores["jogador_01"]['dinheiro'] -= propriedades[casa_atual]['valor']

    #Paga o aluguel
    elif propriedades[casa_atual]['dono'] != None:
        proprietario = propriedades[casa_atual]['dono']
        jogadores["jogador_01"]['dinheiro'] -= propriedades[casa_atual]['aluguel']
        jogadores[proprietario]['dinheiro'] += propriedades[casa_atual]['aluguel']

    #Checa se ainda esta no jogo
    if jogadores["jogador_01"]['dinheiro'] < 0:
        jogadores["jogador_01"]['status'] = 'inativo'
        for i in propriedades:
            if propriedades[i]['dono'] == 'jogador_01':
                propriedades[i]['dono'] = None

"""----------------------------------  jogador 02  ----------------------------------------"""

def jogador_02():
    #Gira o dado e seta o valor da casa atual
    dado = random.randint(1, 6)
    casa_atual = jogadores["jogador_02"].get('casa_atual') + dado

    #Condicional para impedir que a casa_atual passe de 20 e adiciona dinheiro a cada volta no tabuleiro
    if casa_atual > 20:
        casa_atual -= 20
        dinheiro = jogadores["jogador_02"].get('dinheiro')
        jogadores["jogador_02"]['casa_atual'] = casa_atual
        jogadores["jogador_02"]['dinheiro'] = dinheiro + 100
    else:
        jogadores["jogador_02"]['casa_atual'] = casa_atual

    #Checa a possibilidade de compra de acordo com sua personalidade
    if propriedades[casa_atual]['dono'] == None and jogadores["jogador_02"]['dinheiro'] >= propriedades[casa_atual]['valor'] and propriedades[casa_atual]['aluguel'] > 50:

        #Faz a compra da propriedade
        propriedades[casa_atual]['dono'] = 'jogador_02'
        jogadores["jogador_02"]['dinheiro'] -= propriedades[casa_atual]['valor']

    #Paga o aluguel
    elif propriedades[casa_atual]['dono'] != None:
        proprietario = propriedades[casa_atual]['dono']
        jogadores["jogador_02"]['dinheiro'] -= propriedades[casa_atual]['aluguel']
        jogadores[proprietario]['dinheiro'] += propriedades[casa_atual]['aluguel']

    #Checa se ainda esta no jogo
    if jogadores["jogador_02"]['dinheiro'] < 0:
        jogadores["jogador_02"]['status'] = 'inativo'
        for i in propriedades:
            if propriedades[i]['dono'] == 'jogador_02':
                propriedades[i]['dono'] = None

"""----------------------------------  jogador 03  ----------------------------------------"""

def jogador_03():
    #Gira o dado e seta o valor da casa atual
    dado = random.randint(1, 6)
    casa_atual = jogadores["jogador_03"].get('casa_atual') + dado

    #Condicional para impedir que a casa_atual passe de 20 e adiciona dinheiro a cada volta no tabuleiro
    if casa_atual > 20:
        casa_atual -= 20
        dinheiro = jogadores["jogador_03"].get('dinheiro')
        jogadores["jogador_03"]['casa_atual'] = casa_atual
        jogadores["jogador_03"]['dinheiro'] = dinheiro + 100
    else:
        jogadores["jogador_03"]['casa_atual'] = casa_atual

    #Checa a possibilidade de compra de acordo com sua personalidade
    if propriedades[casa_atual]['dono'] == None and jogadores["jogador_03"]['dinheiro'] >= propriedades[casa_atual]['valor'] and  jogadores["jogador_03"]['dinheiro'] - propriedades[casa_atual]['valor'] > 80:

        #Faz a compra da propriedade
        propriedades[casa_atual]['dono'] = 'jogador_03'
        jogadores["jogador_03"]['dinheiro'] -= propriedades[casa_atual]['valor']

    #Paga o aluguel
    elif propriedades[casa_atual]['dono'] != None:
        proprietario = propriedades[casa_atual]['dono']
        jogadores["jogador_03"]['dinheiro'] -= propriedades[casa_atual]['aluguel']
        jogadores[proprietario]['dinheiro'] += propriedades[casa_atual]['aluguel']

    #Checa se ainda esta no jogo
    if jogadores["jogador_03"]['dinheiro'] < 0:
        jogadores["jogador_03"]['status'] = 'inativo'
        for i in propriedades:
            if propriedades[i]['dono'] == 'jogador_03':
                propriedades[i]['dono'] = None


"""----------------------------------  jogador 04  ----------------------------------------"""

def jogador_04():
    #Gira o dado e seta o valor da casa atual
    dado = random.randint(1, 6)
    casa_atual = jogadores["jogador_04"].get('casa_atual') + dado

    #Condicional para impedir que a casa_atual passe de 20 e adiciona dinheiro a cada volta no tabuleiro
    if casa_atual > 20:
        casa_atual -= 20
        dinheiro = jogadores["jogador_04"].get('dinheiro')
        jogadores["jogador_04"]['casa_atual'] = casa_atual
        jogadores["jogador_04"]['dinheiro'] = dinheiro + 100
    else:
        jogadores["jogador_04"]['casa_atual'] = casa_atual

    #Checa a possibilidade de compra de acordo com sua personalidade
    if propriedades[casa_atual]['dono'] == None and jogadores["jogador_04"]['dinheiro'] >= propriedades[casa_atual]['valor']:

        compra = random.uniform(0.0, 1.0)

        if compra > 0.5:
            #Faz a compra da propriedade
            propriedades[casa_atual]['dono'] = 'jogador_04'
            jogadores["jogador_04"]['dinheiro'] -= propriedades[casa_atual]['valor']

    #Paga o aluguel
    elif propriedades[casa_atual]['dono'] != None:
        proprietario = propriedades[casa_atual]['dono']
        jogadores["jogador_04"]['dinheiro'] -= propriedades[casa_atual]['aluguel']
        jogadores[proprietario]['dinheiro'] += propriedades[casa_atual]['aluguel']

    #Checa se ainda esta no jogo
    if jogadores["jogador_04"]['dinheiro'] < 0:
        jogadores["jogador_04"]['status'] = 'inativo'
        for i in propriedades:
            if propriedades[i]['dono'] == 'jogador_04':
                propriedades[i]['dono'] = None

#função reseta valores após encerramento de partidas
def reseta_valores():
    for i in range(1, 21):
        if (i%2) == 0:
            propriedades[i] = {"dono": None, "valor": 100, "aluguel": 40}
        if (i%2) == 1:
            propriedades[i] = {"dono": None, "valor": 120, "aluguel": 55}
    for i in jogadores:
        jogadores[i]['status'] = 'ativo'
        jogadores[i]['casa_atual'] = 0
        jogadores[i]['dinheiro'] = 300

#Iniciando o jogo
def starting_game():
    #setando variaveis p/ calcular as vitorias
    vitorias_totais = 0
    rodada = 0
    vitorias_forcadas = 0
    #interação com o usuário p/ solicitar o inicio do jogo
    jogar = input("Iniciar jogo? (sim/nao): ")

    if jogar == "sim":
        #loop limitado a 300 vitórias
        while vitorias_totais < 300:
            #loop que impede que uma partida dure mais que 1000 rodadas
            while rodada < 1000:
                #inicio de partida respeita a ordem sorteada na variavel "ordem_de_jogo"
                for i in ordem_de_jogo:
                    #Verifica o número de jogadores ativos no jogo
                    jogadores_ativos = [jogadores[jogador].get('status') == 'ativo' for jogador in jogadores]
                    contagem = Counter(jogadores_ativos)
                    #cada jogador joga de acordo com sua vez
                    if i == "jogador_01" and jogadores['jogador_01']['status'] == 'ativo':
                        #verifica se tem mais jogadores ativos no jogo
                        if contagem[True] > 1:
                            jogador_01()
                        #caso o jogador ganhe o jogo
                        else:
                            jogadores['jogador_01']['vitorias'] += 1
                            vitorias_totais += 1
                            rodada += 1
                            turno.append(1)
                            reseta_valores()
                    elif i == "jogador_02" and jogadores['jogador_02']['status'] == 'ativo':
                        #verifica se tem mais jogadores ativos no jogo
                        if contagem[True] > 1:
                            jogador_02()
                        #caso o jogador ganhe o jogo
                        else:
                            jogadores['jogador_02']['vitorias'] += 1
                            vitorias_totais += 1
                            rodada += 1
                            turno.append(1)
                            reseta_valores()
                    elif i == "jogador_03" and jogadores['jogador_03']['status'] == 'ativo':
                        #verifica se tem mais jogadores ativos no jogo
                        if contagem[True] > 1:
                            jogador_03()
                        #caso o jogador ganhe o jogo
                        else:
                            jogadores['jogador_03']['vitorias'] += 1
                            vitorias_totais += 1
                            rodada += 1
                            turno.append(1)
                            reseta_valores()
                    else:
                        if jogadores['jogador_04']['status'] == 'ativo':
                            #verifica se tem mais jogadores ativos no jogo
                            if contagem[True] > 1:
                                jogador_04()
                            #caso o jogador ganhe o jogo
                            else:
                                jogadores['jogador_04']['vitorias'] += 1
                                vitorias_totais += 1
                                rodada += 1
                                turno.append(1)
                                reseta_valores()
                    #seta o número de rodadas
                    if ordem_de_jogo[3] == i:
                        rodada += 1
                turno.append(1)
            #iniciado caso uma partida precise ter parada forçada
            if rodada >= 1000:
                vitorias_forcadas += 1
                saldo_jogador_01 = jogadores['jogador_01']['dinheiro']
                saldo_jogador_02 = jogadores['jogador_02']['dinheiro']
                saldo_jogador_03 = jogadores['jogador_03']['dinheiro']
                saldo_jogador_04 = jogadores['jogador_04']['dinheiro']
                lista_saldo = [saldo_jogador_01, saldo_jogador_02, saldo_jogador_03, saldo_jogador_04]
                vencedor = max(lista_saldo)
                #verifica qual jogador ganhou a partida
                for i in jogadores:
                    if jogadores[i]['dinheiro'] == vencedor:
                        jogadores[i]['vitorias'] += 1
                vitorias_totais += 1
                rodada = 0
                reseta_valores()
        #Inicia a geração dos relatórios
        print(f"O total de partidas terminadas por time out foi de {vitorias_forcadas}")
        print(f"A média de turnos por partida é {len(turno) / vitorias_totais:,.2f}")
        #Mostra a porcentagem de vitorias de cada jogador
        for i in jogadores:
            vitorias = jogadores[i]['vitorias']
            porcentagem = (vitorias * 100) / vitorias_totais
            print(f"Porcentagem de vitórias do {i} -->  {jogadores[i]['personalidade']} | {porcentagem:,.2f}%")
        vitoria_jogador_01 = jogadores['jogador_01']['vitorias']
        vitoria_jogador_02 = jogadores['jogador_02']['vitorias']
        vitoria_jogador_03 = jogadores['jogador_03']['vitorias']
        vitoria_jogador_04 = jogadores['jogador_04']['vitorias']
        lista_vitoria = [vitoria_jogador_01, vitoria_jogador_02, vitoria_jogador_03, vitoria_jogador_04]
        max_vitoria = max(lista_vitoria)

        #filtra personalidade com mais vitorias
        for i in jogadores:
            if jogadores[i]['vitorias'] == max_vitoria:
                print(f"A personalidade com mais vitorias é {jogadores[i]['personalidade']} : {jogadores[i]['vitorias']}")

    else:
        print("Caso queira jogar, inicie o arquivo novamente!")

starting_game()