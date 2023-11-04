
def contaVogal(str):
    vogal = ["a","e","i","o","u","á","é","í","ó","ú","â","ê","î","ô","û","à","è","ì","ò","ù","ã","õ"]
    conta_vogal = 0
    for i in range(len(str)):
        if str[i].lower() in vogal:
            conta_vogal += 1
    return conta_vogal

def ProcuraS (str):
    if "S" in str.upper():
        return True
    else:
        return False

def RemoveA(str):
    str_semA = ""
    for i in str:
        if i != "A":
            str_semA += i
    return str_semA

def Inverte (str):
    texto_invertido = str[::-1]
    return texto_invertido

def QtdePontuacao (str):
    simbolo_ponto = [".", ",", ":", ";", "!", "?"]
    contador = 0

    for letra in str:
        if letra in simbolo_ponto:
            contador += 1 

    return contador

def RemoveLetras (str):
    Novo_Texto = ""
    for letra in str:
        if letra.upper() != "K" and letra.upper() != "W" and letra.upper() != "Y":
            Novo_Texto += letra     
    return Novo_Texto