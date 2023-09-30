'''
1. A lista a seguir contém os dados (Nome, Idade, Setor e Salário) de alguns funcionários de
um hotel. Crie um programa que tenha essa lista.
FuncionariosHotel = [ [ "Guilherme Sá", 26, "Segurança", 852.30 ],
[ "Laura Dias", 31, "Recepção", 715.00 ],
[ "Sônia Lopes", 44, "Lavanderia", 807.90 ],
[ "Roberto Reis", 22, "Garagem", 475.69 ] ]
'''

FuncionariosHotel = [ [ "Guilherme Sá", 26, "Segurança", 852.30 ],
                     [ "Laura Dias", 31, "Recepção", 715.00 ],
                     [ "Sônia Lopes", 44, "Lavanderia", 807.90 ],
                     [ "Roberto Reis", 22, "Garagem", 475.69 ] ]

# a) Alterar o valor do salário da funcionária Laura Dias para R$ 950,14.
FuncionariosHotel[1][3] = 950.14

# b) Acrescentar na lista o funcionário Anísio Nunes, que trabalha no setor Garagem,tem 38 anos e ganha R$ 760,00.
agrupamento = ["Anísio Nunes", 38, "Garagem", 760.00]
FuncionariosHotel.append(agrupamento)

# c) Aumentar o salário de todos os funcionários do setor Lavanderia em 10%.
FuncionariosHotel[2][3] = FuncionariosHotel[2][3] * 1.1

# d) Exibir a idade e o salário do terceiro funcionário da lista.
print(FuncionariosHotel[2][1], FuncionariosHotel[2][3])

# e) Exibir nome e setor de todos os funcionários com menos de 30 anos.
indice = len(FuncionariosHotel)
nome_setor_menos_30 = []
for i in range(indice):
    if FuncionariosHotel[i][1] < 30:
     nome = FuncionariosHotel[i][0]
     setor = FuncionariosHotel[i][2]
     agrupamento = [nome,setor]
     nome_setor_menos_30.append(agrupamento)
print(nome_setor_menos_30)   

# f) Exibir o nome de todos os funcionários do setor de Lavanderia.
funcionario_lavanderia = []
for i in range(indice):
   if FuncionariosHotel[i][2] == "Lavanderia":
      funcionario_lavanderia.append(FuncionariosHotel[i][0])
print(funcionario_lavanderia)

# g) Exibir a média de idade dos funcionários do setor Garagem.

cont_func_garagem = 0
soma_idade = 0
for i in range(indice):
   if FuncionariosHotel[i][2] == "Garagem":
      cont_func_garagem += 1
      soma_idade += FuncionariosHotel[i][1]
media_idade = soma_idade / cont_func_garagem
print(media_idade)

# h) Exibir o nome do funcionário que ganha o maior salário.
maior_salario = FuncionariosHotel[0][3]
nome_maior_salario = ""
for i in range(indice):
   if FuncionariosHotel[i][3] > maior_salario:
      maior_salario = FuncionariosHotel[i][3]
      nome_maior_salario = FuncionariosHotel[i][0]
print(nome_maior_salario)

# i) Exibir a quantidade de funcionários que ganham mais de R$ 700 e têm menos de 40 anos.
cont = 0
for i in range(indice):
   if FuncionariosHotel[i][3] > 700 and FuncionariosHotel[i][1] < 40:
      cont += 1
print(cont)

# j) Exibir o nome do setor que tem o funcionário mais velho.
mais_velho = FuncionariosHotel[0][1]
nome_mais_velho = 0
for i in range(indice):
   if FuncionariosHotel[i][1] > mais_velho:
      mais_velho = FuncionariosHotel[i][1]
      nome_mais_velho = FuncionariosHotel[i][2]
print(nome_mais_velho)

# k) Exibir uma lista com o nome dos funcionários que ganham acima da média salarial da empresa.
soma_total_salario = 0
cont_func = 0
for i in range(indice):
   soma_total_salario += FuncionariosHotel[i][3]
   cont_func += 1
media_total_salario = soma_total_salario / cont_func

lista_func__maior_que_media = []
for i in range(indice):
   if FuncionariosHotel[i][3] > media_total_salario:
      lista_func__maior_que_media.append(FuncionariosHotel[i][0])
print(lista_func__maior_que_media)

print(FuncionariosHotel[0:2])
print(FuncionariosHotel[2:-1])
   