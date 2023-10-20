def defineEstacao (A):
    if A == "JANEIRO" or A == "DEZEMBRO" or A == "FERVEREIRO":
        return "Inverno"
    elif A == "MARÇO" or A == "ABRIL" or A == "MAIO":
        return "Primavera"
    elif A == "JUNHO" or A == "JULHO" or A == "AGOSTO":
        return "Verão"
    else:
        return "Outono"