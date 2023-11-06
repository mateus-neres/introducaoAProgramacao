# 10. A Associação das Senhoras de Terceira Idade precisa de um programa para cadastrar suas 125
# sócias e emitir mensagens periódicas sobre os eventos que realizam. Escreva um programa que
# receba como entrada o nome completo dessas senhoras, no formato Nome Sobrenome1
# Sobrenome2 (Ex: Gabriela Martins Soares), e exiba uma lista, em ordem alfabética, apenas com
# o primeiro sobrenome de cada uma em letras maiúsculas, junto com o título Sra (Ex: Sra
# MARTINS)

import bibiLetras
# nomeCompleto = []
# for i in range(6):
#    nome = input("Digite o nome completo: \n")
#    nomeCompleto.append(nome)
nome = ["Maria Neves Neres","Zefa bezerra Rocha","Joaquina Silva Goma","Antonia Souza Rosario","Luiza Soares Andrade","Juliana Lima Cesar",]

nova_lista = []
for i in range(6):
    nova_lista.append(bibiLetras.nomeMeio(nome[i]))
nova_lista.sort()

print(nova_lista)