'''4) Escreva um programa que utilize as funções da biblioteca criada na questão 2 para receber como
entrada um número e exibir uma mensagem indicando se ele é primo ou não. (Dica: números primos
só são divisíveis por 1 e por eles mesmos)'''

import bibNumeros


numero = int(input("Digite um número para testar se é primo: \n"))
if bibNumeros.contaDivisores(numero) == 2: 
    print(numero)
    print("Primo")
else:
    print(numero)
    print("Não é primo")
    
 