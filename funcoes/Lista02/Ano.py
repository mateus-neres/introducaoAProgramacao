def defineEstacao (A):
    if A == "JANEIRO" or A == "DEZEMBRO" or A == "FERVEREIRO":
        return "Inverno (Vinter)"
    elif A == "MARÇO" or A == "ABRIL" or A == "MAIO":
        return "Primavera (Vâr)"
    elif A == "JUNHO" or A == "JULHO" or A == "AGOSTO":
        return "Verão (Sommar)"
    else:
        return "Outono (Hõst)"