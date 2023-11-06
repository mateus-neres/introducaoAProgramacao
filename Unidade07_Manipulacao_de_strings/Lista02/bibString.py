# 6. Considere a existência de uma função RemoveVogais em uma biblioteca bibString. Essa função
# recebe como entrada um String, remove todas vogais presentes nele, e retorna o String
# restante.

def RemoveVogais(str):
    vogal = ["a","e","i","o","u","á","é","í","ó","ú","â","ê","î","ô","û","à","è","ì","ò","ù","ã","õ"]
    nova_string = ""
    for i in range(len(str)):
        if str[i] not in vogal:
            nova_string += str[i]
    return nova_string