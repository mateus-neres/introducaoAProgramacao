'''
1. Analise cada programa a seguir, de acordo com o que deveria fazer, e aponte os erros nas instruções.
(Dica: utilize valores quaisquer para acompanhar o que os programas estão fazendo)

#################################################################################################

# Programa para ler 20 números e
# exibir a soma dos pares

# Programa refeito                                # programa original
soma = 0
cont = 0                                          # cont = 20
while (cont <= 4):                                # while (cont > 0):
    numero = int(input('Digite um número: '))     #   numero = int (input())
    if numero % 2 == 0:                           #   if (numero % 2):
        soma += numero                            #   soma = numero
    cont += 1                                     #   cont = cont + 1
print(soma)                                       # print(soma)

#################################################################################################

# Programa para ler 30 números e
# exibir a quantidade de positivos

# Programa refeito                                # Programa iriginal
cont = 0                                          # cont = 0
qtdePositivos = 0                                 # qtdePositivos = 0
                                                  # numero = int (input())
while cont <= 4:  
    numero = int(input("Digite um numero: "))     # while (cont > 0):
    if numero >= 0:                               #  if (numero >= 0):
        qtdePositivos += 1                        #      qtdePositivos = numero + 1
    cont = cont + 1                               #  cont = cont + 1
print(qtdePositivos)                              # print(cont)
'''