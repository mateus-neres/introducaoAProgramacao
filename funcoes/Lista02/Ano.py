def defineEstacao (A):
    if A == "janeiro" or A == "dezembro" or A == "fervereiro":
        return "Inverno"
    elif A == "março" or A == "abril" or A == "maio":
        return "Primavera"
    elif A == "junho" or A == "julho" or A == "agosto":
        return "Verão"
    else:
        return "Outono"