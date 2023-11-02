'''
3. Escreva um programa para receber como entrada dois números e exibir a quantidade de
múltiplos de 4 entre eles (os extremos do intervalo não devem ser considerados).   
'''

# Entrada de dados do usuário
numero1 = int(input("Digite o primeiro númeor: "))
numero2 = int(input("Digite o segundo número: "))

# variavel de contagem dos multipls de 4
cont = 0

# Comando condicional para ajustar os valores digitados pelo usuário, caso digite em ordem crescente ou descrecente
if numero1 < numero2:

    # Estrutura de repetições "for"
    for num in range(numero1, numero2):
        # comando condicional para contagem e exibição dos multiplos de 4
        if num % 4 == 0:
            # SAida de dados
            print(num)
            # Contagem dos multiplos de 4
            cont += 1
elif numero1 > numero2 :
    # comando condicional para contagem e exibição dos multiplos de 4
    for num in range(numero1, numero2, -1):
        if num % 4 == 0:
            # SAida de dados
            print(num)
            # Contagem dos multiplos de 4
            cont += 1
# Saida de dados
print(cont)