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
maior_ponto = 0
soma_Ponto_RJ = 0
cont_RJ = 0
indice_maior_ponto = 0

# Listas de registros de dados
lista_times = []
lista_estados = []
lista_pontos = []
lista_pontos_MG = []
lista_Time_PB_PE = []
lista_geral = []

# estrutura de repetição

for i in range(15):

    # Entrada de dados do usuario. OBS: Estou usando as listas de teste para observar o programa. 
    time = times[i]#str(input("Digite o nome do time: "))
    estado = estados[i] #str(input("Digite o estado: "))
    pontos = float(ponto[i]) #float(input("Digite a pontuação do time: "))

    # Listas de armazenamentos de dados de entradas do usuario
    lista_times.append([time])
    lista_estados.append([estado])
    lista_pontos.append([pontos])

    # Junção de todas as listas para exibir ao final do programa
    lista_geral.append(lista_times[i]+lista_estados[i]+lista_pontos[i])

    # estruturas condicionais para o tratamento dos dados e das listas
    if estado == "PB"  and pontos > 100 or estado == "PE" and pontos > 100: # Paramentros para filtrar os times dos estados PB e PE com mais de 100 pontos
        lista_Time_PB_PE.append(time) 

    if estado == "MG": # Parametro para filtrar os times de MG e os pontos do time
        lista_pontos_MG.append([time]+[pontos])

    if estado == "RJ": # Paramentro para filtrar os pontos dos times do estado do RJ
        cont_RJ += 1
        soma_Ponto_RJ += pontos

    if pontos > maior_ponto: # Paramentros para seleção do indice dos time selecionado pelo usuario 
        maior_ponto = pontos
        indice_maior_ponto = i

# Entrada de dados do usuario para seleção do tim
timeUsuario = str(input("Qual o time deseja ver os pontos: "))
indice = lista_times.index([timeUsuario])

# Saidas de dados do desafio
print(lista_geral)
print(f"Times de PE e PB com mais de 100 ponto: {lista_Time_PB_PE}.")
print(f"O time {timeUsuario}, marcou {lista_pontos[indice]}.")
print(f"A lista de pontuação dos times de MG são: {lista_pontos_MG}")
if cont_RJ > 0:
    media_Ponto_RJ = soma_Ponto_RJ / cont_RJ
    print(f"A media dos pontos do RJ é: {media_Ponto_RJ}")
print(f"O nome do time com maior pontuação é: {lista_times[indice_maior_ponto]}")