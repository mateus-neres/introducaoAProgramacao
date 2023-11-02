vogal = ["a","e","i","o","u"]
def conta_vogal(str):
    conta_vogal = 0
    for i in range(len(str)):
        if vogal[i] is str[i]:
            conta_vogal += 1
    return conta_vogal