'''9. Escreva um programa que receba como entrada o nome e o bairro de 500 clientes de uma loja
(guarde em sublistas de uma lista) e exiba no final:
a. A quantidade de clientes que têm sobrenome Silva ou Sousa
b. Apenas o primeiro nome (em letras minúsculas) dos clientes que moram no Centro
c. Os nomes dos bairros (sem repetição) dos clientes cujo nome começa por vogal'''

nomes = ['Wilson', 'Anderson', 'Luis', 'Mateus ', 'Marco', 'Sabrina']
sobreNomes = ["Junior","Silva","Safada","Safada","Souza","Satanas",]
bairros = ['Planalto', 'Agua Fria', 'Centro', 'Manaira', 'Bancarios', 'Mangabeira']

lista_cliente = []
for i in range(6):
    cliente = nomes[i]
    sobreNome = sobreNomes[i]
    bairro = bairros[i]
    agrupamento = (cliente,sobreNome,bairro)
    lista_cliente.append(agrupamento)

contador = 0
for i in range(6):
    if lista_cliente[i][1].upper() == "SILVA" or lista_cliente[i][1].upper() == "SOUZA":
        contador += 1

print(contador)

cliente_centro=[]
for i in range(6):
    if lista_cliente[i][2].upper() == "CENTRO":
        cliente_centro.append(lista_cliente[i][0].lower())
print(cliente_centro)

vogal = ["a","e","i","o","u","á","é","í","ó","ú","â","ê","î","ô","û","à","è","ì","ò","ù","ã","õ"]
nome_bairro = []
for i in range(6):
    if lista_cliente[i][0][0].lower() in vogal:
        nome_bairro.append(lista_cliente[i][2])
print(nome_bairro)