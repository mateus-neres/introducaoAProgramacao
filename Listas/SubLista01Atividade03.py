'''
3) Escreva um programa que receba como entrada e guarde os dados de 10 Estados (Nome, Região,
Quantidade de Municípios, Quantidade de Habitantes) usando uma lista com sublistas. Seu programa
também deve exibir:
a. O nome de todos os Estados da Região Sul.
b. A quantidade de Estados da Região Nordeste com mais de 100 municípios.
c. A quantidade total de cidades dos Estados da Região Norte.
d. A quantidade de Estados da Região Centro-Oeste com menos de 500 mil habitantes.
e. A quantidade média de habitantes dos Estados da Região Sudeste.
Exemplo de conteúdo da lista:
Estados = [ [ "Paraíba", "Nordeste", 223, 3944000 ], [ "Goiás", "Centro-Oeste", 246, 6523000 ], [ "Pará",
"Norte", 144, 8074000 ], ...]
'''

teste_estados = ['SP', 'MG', 'RJ', 'BA', 'RS', 'PR', 'PE', 'CE', 'PA', 'SC']
teste_regiao = ['Sudeste', 'Sudeste', 'Sudeste', 'Nordeste', 'Sul', 'Sul', 'Nordeste', 'Nordeste', 'Norte', 'Sul']
teste_municipios = [645, 853, 92, 417, 497, 399, 184, 184, 144, 295]
teste_populacao = [46065000, 21041000, 17046000, 15041000, 11048000, 11057000, 9062000, 9029000, 8069000, 7028000]

quantidade_de_estado = int(input())
lista_geral = []
for i in range(quantidade_de_estado):
    estado = str.upper(teste_estados[i]) # str.upper(input("Digite o nome do estado: "))
    regiao = str.upper(teste_regiao[i]) # str.upper(input("Digite o nome da região: "))
    municipios = int(teste_municipios[i]) # int(input("Digite a quantidade de municipios: "))
    populacao = int(teste_populacao[i]) # int(input("Digite a população do estado: "))

    agrupamento = [estado, regiao, municipios, populacao]
    lista_geral.append(agrupamento)

# a. O nome de todos os Estados da Região Sul.
lista_estados_sul = []
for i in range(quantidade_de_estado):
    if lista_geral[i][1] == "SUL":
        lista_estados_sul.append(lista_geral[i][0])

# b. A quantidade de Estados da Região Nordeste com mais de 100 municípios.
for i in range(quantidade_de_estado):
    if lista_geral[i][]


print(lista_geral)
print(f"Estados da região SUL: {lista_estados_sul}")