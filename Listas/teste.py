listona = [[[4, 10, 18],[1, 2, 3]],
           [[14], [4, 5, 6]],
           [[3, 7, 2], [7, 8, 9]],
           [[16], [10, 11, 12]],
           [[30], [13, 14, 15]],
           [[9, 5], [9, 5]],
           [[12], [12]]]

Lista = [[4, 10, 18],
         14,
         [3, 7, 2],
         16, 
         30,
         [9, 5], 
         12]

lista = [[1,2,3],
         [4,5,6],
         [7,8,9],
         [10,11,12],
         [13,14,15],
         [9, 5], 
         [12]]

lista_elemento = [[1,2],2,3,4,5,6,7,8,9,10]
lista_elemento1 = ["a","b","c","d",["e","t"],"f","g","h","i","j"]
lista_geral = []
indice = len(Lista)
for i in range(indice):
    agrupamento = [Lista[i], lista[i]]
    lista_geral.append(agrupamento)

print(Lista[2][0])
print(lista[2][0])
print(lista_geral[4][1])


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

print(lista_geral[3][2])