'''a) Uma função testaMultiplo4 que receba por parâmetro um número inteiro e retorne verdadeiro se
ele for múltiplo de 4, ou falso caso contrário.'''

def testaMultiplo4 (A):
    if A % 4 == 0:
        return True
    else:
        return False

'''b) Uma função contaDivisores que receba como parâmetro um número inteiro, e retorne a
quantidade de divisores que ele tem. (Dica: lembre-se de que não é possível dividir por zero)
'''
def contaDivisores(A):
    contDiv = 0
    for i in range(A+1):
        if  i != 0 and A % i == 0:
            contDiv += 1
    return contDiv