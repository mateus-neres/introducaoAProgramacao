'''
4. Uma empresa tem 10 funcionários com cargos e salários diferentes. Ela resolveu dar um
aumento de 20% no salário apenas para os funcionários dos setores Recursos Humanos e
Almoxarifado. Escreva um programa que receba como entrada e armazene em duas listas
diferentes os setores e salários de todos os funcionários, calcule o aumento concedido
para os funcionários dos setores contemplados, e depois exiba apenas os salários
modificados. O programa deve exibir também quanto dinheiro extra a empresa vai gastar
depois do aumento. (Dica: teste o programa apenas para 3 entradas)
'''
# Listas de destes
lista_teste_setores = ["RH","produção","RH","RH","produção","produção","almoxarifado","almoxarifado","produção","almoxarifado"]
lista_teste_salario = [1800,1400,1800,1800,1400,1400,1600,1600,1400,1600]

# Lista para armazenamento de dados


adicional_total = 0
lista_geral = []
# Estrutura de repetição
for i in range(10):

    # Entrada de dados do usuario OBS: Utilizei as listas de teste apenas para testar e observar o programa em uso
    setor = str.upper(lista_teste_setores[i]) # str(input("Digite o setor: "))
    salario = lista_teste_salario[i] # float(input("Digite o salario: "))
    lista_agrupamento = [setor,salario]
    lista_geral.append(lista_agrupamento)

    # Comando condicional para filtrar os setores com aumentos salariais
lista_RH_Almoxarifado = []
for i in range(10):
    if lista_geral[i][0] == "RH" or lista_geral[i][0] == "ALMOXARIFADO":
        lista_RH_Almoxarifado.append(lista_geral[i][1] * 1.2)
        adicional_total += (lista_geral[i][1] * 0.2)

# Saida de dados 
print(f"Os novos Salários serão de: {lista_RH_Almoxarifado}")
print(f"os gastos da empresa, almentaram em {adicional_total}")
