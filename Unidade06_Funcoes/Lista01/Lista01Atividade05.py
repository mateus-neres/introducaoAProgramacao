'''
5) Crie uma biblioteca chamada bibLetras, e crie nela uma função testaVogal que receba por parâmetro
um caractere e retorne verdadeiro se ele for uma vogal, ou falso caso contrário. (Dica: Lembre-se que
as vogais podem aparecer acentuadas com  ́, ^, ` ou ~.)
'''

import bibLetras

vogal = str.lower(input("Digite uma letra, para verificar se é vogal ou não: \n"))
print(bibLetras.testaVogal(vogal))