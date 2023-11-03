
def contaVogal(str):
    vogal = ["a","e","i","o","u"]
    conta_vogal = 0
    for i in range(len(str)):
        if str[i].lower() in vogal:
            conta_vogal += 1
    return conta_vogal