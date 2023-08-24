'''
5. Um restaurante self-service de Rio Tinto cobra R$ 40 por quilo nas refeições. Sabendo que, na hora
de determinar o valor da refeição, deve ser desconsiderado o peso do prato vazio (230 gramas),
escreva um programa que receba como entrada o peso total do prato de um cliente em gramas e
exiba o preço cobrado com duas casas decimais. (Lembrete: 1 quilo = 1000 gramas)
'''

# Constantes

tara_prato = 230 #Em gramas
valor_quilo = 40 #Em reais
quiloGrama = 1000 #Em gramas

# Entrada de dados:

peso_prato = input('Qual o peso do prato em gramas: ')

# Tratamento de dados: 

peso_prato_int = int(peso_prato)

valor_a_pagar = (valor_quilo / quiloGrama) * (peso_prato_int - tara_prato)

# Saída de dados:

print(f'O valor a ser pago será R${valor_a_pagar:.2f}')
