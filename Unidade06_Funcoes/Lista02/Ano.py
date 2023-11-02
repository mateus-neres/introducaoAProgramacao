def defineEstacao (A):
    if A.lower() == "janeiro" or A.lower() == "dezembro" or A.lower() == "fervereiro":
        return "Inverno"
    elif A.lower() == "março" or A.lower() == "abril" or A.lower() == "maio":
        return "Primavera"
    elif A.lower() == "junho" or A.lower() == "julho" or A.lower() == "agosto":
        return "Verão"
    else:
        return "Outono"