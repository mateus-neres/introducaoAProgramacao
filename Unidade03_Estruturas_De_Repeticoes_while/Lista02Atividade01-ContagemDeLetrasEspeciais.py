# 1. Escreva um programa que receba como entrada várias letras, até que seja informada a letra X (ou x) e exiba
# quantas vezes foram lidas as letras especiais K, Y e W.
# Dica: as letras podem ser informadas em maiúsculas ou minúsculas.

# entrada de dados: 

contagem = 0
letra = str.upper(input('Digite uma letra: ')) # step 1

# tratamento de dados: 

while letra != 'X': # step 2 
    if letra == 'K' or letra == 'Y' or letra == 'W': # step 3
        contagem += 1 # step 4 
        print(f'Já foram {contagem} letras especiais') # Step 5 
    letra = str.upper(input('Digite uma letra: ')) # Step 6 
print(contagem)
print('Acabou')



