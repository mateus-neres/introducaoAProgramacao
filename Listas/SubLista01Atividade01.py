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

Lista = [ [4, 10, 18], 14, [3, 7, 2], 16, 30, [9, 5], 12 ]

Lista [0] = [Lista [6]] + Lista [0]

print(Lista [5][1])