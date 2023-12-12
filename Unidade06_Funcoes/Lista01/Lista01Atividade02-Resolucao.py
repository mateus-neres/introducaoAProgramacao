#2) Crie uma biblioteca chamada bibNumeros, e crie nela:

import bibNumeros

'''a) Uma função testaMultiplo4 que receba por parâmetro um número inteiro e retorne verdadeiro seele for múltiplo de 4,
ou falso caso contrário.'''

a = int(input("Digite um número para verificar se ele é multiplo de 4:\n"))
print(f"{bibNumeros.testaMultiplo4(a)}")

'''b) Uma função contaDivisores que receba como parâmetro um número inteiro, e retorne a
quantidade de divisores que ele tem. (Dica: lembre-se de que não é possível dividir por zero)'''

b = int(input("Digite um número para verificar a quantidade de divisores: \n"))
print(f"Quantidade de divisões exatas: {bibNumeros.contaDivisores(b)}")
