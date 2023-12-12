'''
1) A lista abaixo contém dados diversos. Mostre como ficará seu conteúdo após cada comando (obs:
considere a execução de cada comando sempre na lista original)
Lista = [ [4, 10, 18], 14, [3, 7, 2], 16, 30, [9, 5], 12 ]

a. Lista [2].append ( Lista [4] )
b. Lista [0] = [Lista [6]] + Lista [0]
c. Lista [5][1] += Lista [0] [1] + Lista [2] [1]
d. Lista.append ( [ Lista [4], Lista [1] ] )
e. Lista [0] += [ Lista [5] [0] ] + [ Lista [2] [2] ]

'''
listona = [[[1, 2, 3], [4, 10, 18]],[[4, 5, 6], [14]],[[7, 8, 9], [3, 7, 2]],[[10, 11, 12], [16]],[[13, 14, 15], [30]]]

Lista = [[4, 10, 18],[14],[3, 7, 2],[16], [30],[9, 5], [12]]

lista = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]

lista_geral = []
len(lista)
for i in range(len(lista)):
    agrupamento = [lista[i], Lista[i]]
    lista_geral.append(agrupamento)

print(Lista[2][0])
print(lista[2][0])
print(lista_geral[4][1])