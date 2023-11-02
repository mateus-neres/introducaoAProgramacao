#1. A lista a seguir contém os dados (Nome, Idade, Setor e Salário) de alguns funcionários de um hotel. Crie um programa que tenha essa lista.
FuncionariosHotel = [["Guilherme Sá", 26, "Segurança", 852.30],
                     ["Laura Dias", 31, "Recepção", 715.00],
                     ["Sônia Lopes", 44, "Lavanderia", 807.90],
                     ["Roberto Reis", 22, "Garagem", 475.69]]

#2. Considerando essa lista, escreva os comandos necessários para:

# a) Alterar o valor do salário da funcionária Laura Dias para R$ 950,14.
FuncionariosHotel[1][3] = 950.14
print(FuncionariosHotel)

# b) Acrescentar na lista o funcionário Anísio Nunes, que trabalha no setor Garagem, tem 38 anos e ganha R$ 760,00.
funcionario_novo = ["Anísio Nunes", 38, "Garagem", 760.00]
FuncionariosHotel.append(funcionario_novo)
print(FuncionariosHotel)

# c) Aumentar o salário de todos os funcionários do setor Lavanderia em 10%.
indice = len(FuncionariosHotel)
for repeticao in range(indice):
   if FuncionariosHotel[repeticao][2].upper() == "LAVANDERIA":
       FuncionariosHotel[repeticao][3] = FuncionariosHotel[repeticao][3] * 1.1
print(FuncionariosHotel)

# d) Exibir a idade e o salário do terceiro funcionário da lista. Resultado esperado: 44 888,69
idade_salario = []
for repeticao in range(indice):
    if repeticao == 2:
         agrupamento = [FuncionariosHotel[repeticao][1], FuncionariosHotel[repeticao][3]]
         idade_salario.append(agrupamento)
print(idade_salario)

# e) Exibir nome e setor de todos os funcionários com menos de 30 anos. Resultado esperado: Guilherme Sá Segurança Roberto Reis Garagem
nome_menor_trinta = []
for repeticao in range(indice):
    if FuncionariosHotel[repeticao][1] < 30:
        agrupamento = [FuncionariosHotel[repeticao][0], FuncionariosHotel[repeticao][2]]
        nome_menor_trinta.append(agrupamento)
print(nome_menor_trinta)

# f) Exibir o nome de todos os funcionários do setor de Lavanderia. Resultado esperado: Sônia Lopes
nome_fincionario_lavanderia = []
for repeticao in range(indice):
    if FuncionariosHotel[repeticao][2].upper() == "LAVANDERIA":
        nome_fincionario_lavanderia.append(FuncionariosHotel[repeticao][0])
print(nome_fincionario_lavanderia)

# g) Exibir a média de idade dos funcionários do setor Garagem. Resultado esperado: 30
soma_idade = 0
cont_idade = 0
for repeticao in range(indice):
    if FuncionariosHotel[repeticao][2].upper() == "GARAGEM":
        soma_idade += int(FuncionariosHotel[repeticao][1])
        cont_idade += 1
media_idade = soma_idade // cont_idade
print(media_idade)
    
# h) Exibir o nome do funcionário que ganha o maior salário. Resultado esperado: Laura Dias
nome_maior_salario = ""
maior_salario = FuncionariosHotel[0][3]
for repeticao in range(indice):
    if FuncionariosHotel[repeticao][3] > maior_salario:
        maior_salario = FuncionariosHotel[repeticao][3]
        nome_maior_salario = FuncionariosHotel[repeticao][0]
print(nome_maior_salario)

# i) Exibir a quantidade de funcionários que ganham mais de R$ 700 e têm menos de 40 anos. Resultado esperado: 3
cont_maior_700 = 0
for repeticao in range(indice):
    if FuncionariosHotel[repeticao][3] > 700 and FuncionariosHotel[repeticao][1] < 40:
        cont_maior_700 += 1
print(cont_maior_700)

# j) Exibir o nome do setor que tem o funcionário mais velho. Resultado esperado: Lavanderia
setor_funcionario_mais_velho = ""
maior_idade = FuncionariosHotel[0][1]
for repeticao in range(indice):
    if FuncionariosHotel[repeticao][1] > maior_idade:
        maior_idade = FuncionariosHotel[repeticao][1]
        setor_funcionario_mais_velho = FuncionariosHotel[repeticao][2]
print(setor_funcionario_mais_velho)

# k) Exibir uma lista com o nome dos funcionários que ganham acima da média salarial da empresa. Resultado esperado: [“Guilherme Sá”, “Laura Dias”, “Sônia Lopes”]
soma_salario = 0
cont_salario = 0
for repeticao in range(indice):
    soma_salario += FuncionariosHotel[repeticao][3]
    cont_salario += 1
media = soma_salario / cont_salario
nome_salario_maior_media = []
for repeticao in range(indice):
    if FuncionariosHotel[repeticao][3] > media:
        nome_salario_maior_media.append(FuncionariosHotel[repeticao][0])
print(nome_salario_maior_media)