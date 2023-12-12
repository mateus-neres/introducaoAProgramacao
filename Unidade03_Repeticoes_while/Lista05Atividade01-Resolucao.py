'''
1. Escreva um programa que receba como entrada a idade de várias pessoas, até que seja informada uma idade
negativa, e exiba a quantidade de pessoas jovens, a maior idade registrada para um adulto, e a média de idade
dos idosos, de acordo com a classificação abaixo (Dica: Considere a maior idade inicial para os adultos como zero):
'''
contadorIdoso = 0
quantidadejovem = 0
maiorIdadeAdulto = 0
somaIdadeIdoso = 0
idade = int(input("Digite a idade: "))
while idade >= 0:
    if idade >= 0 and idade < 20:
        quantidadejovem += 1
    elif idade >= 20 and idade < 60:
        if idade > maiorIdadeAdulto:
            maiorIdadeAdulto = idade
    else:
        somaIdadeIdoso += idade
        contadorIdoso += 1
    idade = int(input("Digite a Idade: "))
if quantidadejovem > 0:
    print(f"A quantidade de jovem é de -> {quantidadejovem}")
else:
    print("Não há jovem")
if maiorIdadeAdulto > 0:
    print(f"A maior idade entre os adultos é de -> {maiorIdadeAdulto}")
else:
    print("Não há Adultos")
if contadorIdoso == 0:
    print("Não há idoso")
else:
    mediaIdadeIdoso = somaIdadeIdoso / contadorIdoso 
    print(f"A media de idade entre os idosos é de {mediaIdadeIdoso:.0f}")
