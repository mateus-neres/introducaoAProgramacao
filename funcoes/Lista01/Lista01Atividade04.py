'''
4) Escreva um programa que utilize as funções da biblioteca criada na questão 2 para receber como
entrada um número e exibir uma mensagem indicando se ele é primo ou não. (Dica: números primos
só são divisíveis por 1 e por eles mesmos)
'''

import bibNumeros

teste1 = [7, 4, 51, 43]
for i in range(len(teste1)):
    numero = bibNumeros.contaDivisores(teste1[i])
    if numero == 2: 
        print(teste1[i])
        print("Primo")
    else:
        print(teste1[i])
        print("Não é primo")
    
 