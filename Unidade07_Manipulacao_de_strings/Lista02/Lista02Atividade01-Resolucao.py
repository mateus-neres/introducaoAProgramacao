# 1. Escreva uma função contemVogal que receba como parâmetro um string e retorne
# True caso ele contenha alguma vogal, ou False caso contrário.

def contemVogal(str):
    vogal = ["a","e","i","o","u","á","é","í","ó","ú","â","ê","î","ô","û","à","è","ì","ò","ù","ã","õ"]
    for i in range(len(str)):
        if str[i] in vogal:
            return True
    return False