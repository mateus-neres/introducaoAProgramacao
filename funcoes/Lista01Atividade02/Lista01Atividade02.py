'''
2) Crie uma biblioteca chamada bibNumeros, e crie nela:
a) Uma função testaMultiplo4 que receba por parâmetro um número inteiro e retorne verdadeiro se
ele for múltiplo de 4, ou falso caso contrário.


b) Uma função contaDivisores que receba como parâmetro um número inteiro, e retorne a
quantidade de divisores que ele tem. (Dica: lembre-se de que não é possível dividir por zero)

'''

import bibNumeros


numA = int(input())
numB= numA

a = bibNumeros.testaMultiplo4(numA)

print(a)

b = bibNumeros.contaDivisores(numB)

print(b)