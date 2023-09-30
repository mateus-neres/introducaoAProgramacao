'''
2) Fernanda deseja gerenciar melhor suas finanças. Ela precisa registrar, a cada mês, o total de suas
receitas (dinheiro recebido) e o total de suas despesas (dinheiro gasto) para fazer um balanço do que
precisa ser modificado em seu orçamento.
Crie uma única lista Orçamento2017, em que cada elemento será uma lista composta por três dados
(mês, receita, despesa). Em seguida, faça o que se pede. Veja o modelo:
Orcamento2017 = [["Janeiro", 2020, 1570], ["Fevereiro", 1895.70, 1450.25]]
a. Exiba o total recebido nos 5 primeiros meses.
b. Exiba o nome dos meses em que a despesa foi superior a R$ 2500.
c. Exiba a quantidade de meses em que a receita foi maior que a despesa.
d. Exiba o nome do mês em que houve a maior despesa.
e. Exiba a receita média anual.
'''
mes_teste = ["janeiro","fervereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
receita_teste = [1000,1002,2100,5222,3063,8542,6663,4121,3221,6333,4423,5426]
despesas_teste = [1200,1040,2020,5122,3003,8442,6763,4321,3321,6433,4563,5926]

lista_geral = []
for i in range(12):
    mes = str.upper(mes_teste[i]) #str.upper(input("Digite o mês: "))
    receita = float(receita_teste[i]) #float(input("Digite a receita do mês: "))
    despesas = float(despesas_teste[i]) #float(input("Digite as despesas do mês: "))
    agrupamento = [mes, receita, despesas]
    lista_geral.append(agrupamento)

somas_5_mese = 0
for i in range(5):
    somas_5_mese += lista_geral[i][1]

meses_maior_2500 = []
for i in range(12):
    if lista_geral[i][2] > 2500:
        meses_maior_2500.append(lista_geral[i][0])

meses_receita_maior_despesa = []
for i in range(12):
    if lista_geral[i][1] > lista_geral[i][2]:
        meses_receita_maior_despesa.append(lista_geral[i][0])

maior_despesa = lista_geral[0][2]
mes_maior_despesa = []
for i in range(12):
    if lista_geral[i][2] > maior_despesa:
        maior_despesa = lista_geral[i][2]
        mes_maior_despesa = lista_geral[i][0]

soma_receita = 0
cont = 0
for i in range(12):
    soma_receita += lista_geral[i][1]

media_receita_anual = soma_receita / 12

print(lista_geral)
print(f"O total recebido nos 5 primeiros meses é: R${somas_5_mese:.2f}")
print(f"os meses com despesas maiores que R$2500, foram: {meses_maior_2500}")
print(f"Os meses que a receita, foram maior que as despesas são: {meses_receita_maior_despesa}")
print(f"Os mês com maior despesa foi: {mes_maior_despesa}")
print(f"A media Anual da receita é de: R${media_receita_anual:.2f}")