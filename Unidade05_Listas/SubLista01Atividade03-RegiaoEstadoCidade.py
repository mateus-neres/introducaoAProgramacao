'''
3) Escreva um programa que receba como entrada e guarde os dados de 10 Estados (Nome, Região,
Quantidade de Municípios, Quantidade de Habitantes) usando uma lista com sublistas. Seu programa
também deve exibir:
a. O nome de todos os Estados da Região Sul.
b. A quantidade de Estados da Região Nordeste com mais de 100 municípios.
c. A quantidade total de cidades dos Estados da Região Norte.
d. A quantidade de Estados da Região sul com menos de 500 mil habitantes.
e. A quantidade média de habitantes dos Estados da Região Sudeste.
Exemplo de conteúdo da lista:
Estados = [ [ "Paraíba", "Nordeste", 223, 3944000 ], [ "Goiás", "Centro-Oeste", 246, 6523000 ], [ "Pará",
"Norte", 144, 8074000 ], ...]
'''

teste_estados = ['SP', 'MG', 'RJ', 'BA', 'RS', 'PR', 'PE', 'CE', 'PA', 'SC']
teste_regiao = ['Sudeste', 'Sudeste', 'Sudeste', 'Nordeste', 'Sul', 'Sul', 'Nordeste', 'Nordeste', 'Norte', 'Sul']
teste_municipios = [645, 853, 92, 417, 497, 399, 184, 184, 144, 295]
teste_populacao = [46065000, 21041000, 17046000, 15041000, 11048000, 11057000, 9062000, 9029000, 8069000, 7028000]


lista_geral = []
for i in range(10):
    estado = str.upper(teste_estados[i]) # str.upper(input("Digite o nome do estado: "))
    regiao = str.upper(teste_regiao[i]) # str.upper(input("Digite o nome da região: "))
    municipios = int(teste_municipios[i]) # int(input("Digite a quantidade de municipios: "))
    populacao = int(teste_populacao[i]) # int(input("Digite a população do estado: "))

    agrupamento = [estado, regiao, municipios, populacao]
    lista_geral.append(agrupamento)

# a. O nome de todos os Estados da Região Sul.
lista_estados_sul = []
for i in range(10):
    if lista_geral[i][1] == "SUL":
        lista_estados_sul.append(lista_geral[i][0])

# b. A quantidade de Estados da Região Nordeste com mais de 100 municípios.
cont_estados_nordeste = 0
for i in range(10):
    if lista_geral[i][1] == "NORDESTE":
        cont_estados_nordeste += lista_geral[i][2]

# c. A quantidade total de cidades dos Estados da Região Norte.
cont_cidades_norte = 0
for i in range(10):
    if lista_geral[i][1] == "NORTE":
        cont_cidades_norte += lista_geral[i][2]

# d. A quantidade de Estados da Região sul com menos de 500 mil habitantes.
cont_estados_sul = 0
for i in range(10):
    if lista_geral[i][1] == "SUL" and lista_geral[i][3] < 500000:
        cont_estados_nordeste += 1

# e. A quantidade média de habitantes dos Estados da Região Sudeste.
cont_habt_sudest = 0
cont_estados_sudeste = 0
for i in range(10):
    if lista_geral[i][1] == "SUDESTE":
        cont_habt_sudest += lista_geral[i][3]
        cont_estados_sudeste += 1

media_habt_sudeste = cont_habt_sudest / cont_estados_sudeste


print(lista_geral)
print(f"Estados da região SUL: {lista_estados_sul}")
print(f"Há {cont_estados_nordeste} estados com mais de 100 mil habitantes no nordeste!")
print(f"Ha {cont_cidades_norte} municipios na região Norte!")
print(f"A media de habitantes do suldeste por estado é de: {media_habt_sudeste:.0f}")
