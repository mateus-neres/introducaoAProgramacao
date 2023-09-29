'''
3. Vai ser realizado um campeonato de futebol, e você precisa escrever um programa que
receba como entrada o nome, o Estado e a quantidade de pontos de vários times (a
quantidade deve ser informada pelo usuário), e armazenar essas informações em listas.
Esse programa deverá também exibir:

- Os nomes de todos os times de PB e PE com mais de 100 pontos
- A quantidade de pontos de um time informado pelo usuário
- A lista de pontuações dos times de MG
- A média de pontos dos times do RJ
- O nome do time que teve a maior pontuação
'''

# Listas de testes 
times = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",]
estados = ["BP","PE","RJ","SP","MG","PB","PE","MG","RJ","SP","RJ","PB","RJ","SP","MG"]
ponto = [101,120,90,80,200,140,110,130,125,112,110,50,80,98,100]

# variaveis de controle
soma_Ponto_RJ = 0
cont_RJ = 0

# Listas de registros de dados
lista_pontos_MG = []
lista_Time_PB_PE = []
lista_geral = []
ponto_time_escolhido = 0
# estrutura de repetição

for i in range(15):

    # Entrada de dados do usuario. OBS: Estou usando as listas de teste para observar o programa. 
    time = str.upper(times[i]) #str(input("Digite o nome do time: ")).upper()
    estado = str.upper(estados[i]) #str(input("Digite o estado: ")).upper()
    pontos = int(ponto[i]) #float(input("Digite a pontuação do time: "))

    # Junção de todas as listas para exibir ao final do programa
    lista_agrupamento = [time, estado, pontos]
    lista_geral.append(lista_agrupamento)

    # estruturas condicionais para o tratamento dos dados e das listas
for i in range(15):
    if lista_geral[i][1] == "PB" and lista_geral[i][2] > 100 or lista_geral[i][1] == "PE" and lista_geral[i][2] > 100: # Paramentros para filtrar os times dos estados PB e PE com mais de 100 pontos
        lista_Time_PB_PE.append(lista_geral[i][0] + lista_geral[i][1]) 

timeUsuario = str.upper(input("Qual o time deseja ver os pontos: "))

for i in range(15):
    if lista_geral[i][0] == timeUsuario:
        ponto_time_escolhido = lista_geral[i][2]

for i in range(15):
    if lista_geral[i][1] == "MG": # Parametro para filtrar os times de MG e os pontos do time
        lista_pontos_MG.append(lista_geral[i][2])

for i in range(15):
    if lista_geral[i][1] == "RJ": # Paramentro para filtrar os pontos dos times do estado do RJ
        cont_RJ += 1
        soma_Ponto_RJ += lista_geral[i][2]

media_Ponto_RJ = soma_Ponto_RJ / cont_RJ


maior_ponto = lista_geral[0][2]
maior_ponto_time = 0
for i in range(15):
    if lista_geral[i][2] > maior_ponto:
        maior_ponto = lista_geral[i][2]
        maior_ponto_time = lista_geral[i][0]

# Saidas de dados do desafio
print(lista_geral)
print(f"Times de PE e PB com mais de 100 ponto: {lista_Time_PB_PE}.")
print(f"O time {timeUsuario}, marcou {ponto_time_escolhido}.")
print(f"A lista de pontuação dos times de MG são: {lista_pontos_MG}")
print(f"A media dos pontos do RJ é: {media_Ponto_RJ}")
print(f"O nome do time com maior pontuação é: {maior_ponto_time}")