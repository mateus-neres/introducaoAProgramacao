
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
