'''
2) Crie uma biblioteca chamada bibNumeros, e crie nela:
a) Uma função testaMultiplo4 que receba por parâmetro um número inteiro e retorne verdadeiro se
ele for múltiplo de 4, ou falso caso contrário.


b) Uma função contaDivisores que receba como parâmetro um número inteiro, e retorne a
quantidade de divisores que ele tem. (Dica: lembre-se de que não é possível dividir por zero)

'''

import bibNumeros

teste1 = [4, 7, -16, 4, 5, 18, 0]
for i in range(len(teste1)):
    a = bibNumeros.testaMultiplo4(teste1[i])
    b = bibNumeros.contaDivisores(teste1[i])
    print(f"Numero testado: {teste1[i]}")
    print(f"Divisivel por 4?: {a}")
    print(f"Quantidade de divisões exatas: {b}")
