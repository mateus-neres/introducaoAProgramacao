'''
5) Crie uma biblioteca chamada bibLetras, e crie nela uma função testaVogal que receba por parâmetro
um caractere e retorne verdadeiro se ele for uma vogal, ou falso caso contrário. (Dica: Lembre-se que
as vogais podem aparecer acentuadas com  ́, ^, ` ou ~.)
'''

import bibLetras

teste1 = ["A", "o", "G", "5", "ã"]
 
for i in range(len(teste1)):
    vogal = str.lower(teste1[i])
    print(vogal)
    print(bibLetras.testaVogal(vogal))