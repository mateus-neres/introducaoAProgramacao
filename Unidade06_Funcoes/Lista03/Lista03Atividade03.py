'''3. Escreva um programa que receba como entrada os nomes de 30 obras e exiba quantas esculturas
de Adélia Machado existem na galeria.'''
import bibGaleriaArte

escuturasAdelia = 00
for i in range(5):
    entrada = input()
    if(bibGaleriaArte.consultaArtista(entrada) == "Adélia Machado"):
        if(bibGaleriaArte.consultaTipo(entrada) == "Escultura"):
            escuturasAdelia += 1

print(escuturasAdelia)