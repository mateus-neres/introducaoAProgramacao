import bibGaleriaArte

preco = 0
for i in range(60):
    entrada = input("Nome da obra:\n")
    if(bibGaleriaArte.consultaArtista(entrada).upper() == "LEONARDO RESENDE"):
        preco += bibGaleriaArte.consultaPreco(entrada)
print(preco)
