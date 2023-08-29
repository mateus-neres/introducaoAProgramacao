'''
1. Elza precisa comprar um presente para sua filha e foi a uma loja que vende bolsas e relógios. As bolsas
de couro custam R$ 180, e as de tecido custam R$ 100. Já os relógios com pulseira de metal custam R$
215, e os com pulseira de couro custam R$ 150. Sabendo que a loja oferece como brinde um chaveiro
na compra de qualquer relógio, escreva um programa que receba como entrada os dados do presente
escolhido por Elza (tipo e material), e exiba o valor a ser pago e uma mensagem informando se ela
ganhou o brinde ou não.
'''

bolsa_couro = 180
bolsa_tecido = 100
relogio_metal = 215
relogio_couro = 150

tipo = str.upper(input('Digite o tipo de presente, relogio ou bolsa: '))

if tipo == 'RELOGIO':

    material = str.upper(input('Digite o material do relogio, couro ou metal: '))

    if material == 'METAL':
        print(f'O valor do presente será de R${relogio_metal:.2f} e você recebe um chaveiro.')

    elif material == 'COURO':
        print(f'O valor do presente será de R${relogio_couro:.2f} e você recebe um chaveiro.')

elif tipo == 'BOLSA':

    material = str.upper(input('Digite o material do relogio, couro ou metal: '))

    if material == 'COURO':
        print(f'O valor do presente é de R${bolsa_couro:.2f}.')

    elif material == 'TECIDO':
        print(f'O valor do presente será de R${bolsa_tecido:.2f}.')


