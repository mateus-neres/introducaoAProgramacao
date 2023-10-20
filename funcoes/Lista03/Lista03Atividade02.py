'''
2. Escreva um programa que receba como entrada os nomes de 50 obras da galeria e exiba uma
mensagem informando se ela dispõe de uma quantidade maior de quadros ou de esculturas.
'''

teste1 = [['Mona Lisa', 'Leonardo da Vinci', 'Pintura', 5825], ['A Noite Estrelada', 'Vincente Van Gogh', 'Pintura', 8636], ['A Última Ceia', 'Leonardo da Vinci', 'Pintura', 7752], ['O Nascimento de Vênus', 'Sandro Botticelli', 'Pintura', 8723], ['Guernica', 'Pablo Picasso', 'Pintura', 8530], ['O Beijo', 'Gustav Klimt', 'Pintura', 6915], ['O Grito', 'Edvard Munch', 'Pintura', 6923], ['A Persistência da Memória', 'Salvador Dalí', 'Pintura', 9765], ['Os Girassóis', 'Vincent van Gogh', 'Pintura', 9827], ['A Criação de Adão', 'Michelangelo', 'Pintura', 8951], ["Os Lírios D'Água", 'Claude Monet', 'Pintura', 7124], ['A Moça com o Brinco de Pérola', 'Johannes Vermeer', 'Pintura', 7210], ['A Liberdade Guiando o Povo', 'Eugène Delacroix', 'Pintura', 8947], ['Noite Estrelada sobre o Ródano', 'Vincent van Gogh', 'Pintura', 6531], ['Auto-Retrato com Macaco', 'Frida Kahlo', 'Pintura', 5038], ['O Gato e o Canário', 'Franz Marc', 'Pintura', 9983], ['Os Meninos de Varberg', 'Bruno Liljefors', 'Pintura', 5891], ['Crepúsculo', 'Caspar David Friedrich', 'Pintura', 9206], ['Primavera', 'Édouard Manet', 'Pintura', 9316], ['A Ronda Noturna', 'Rembrandt', 'Pintura', 9485], ['A Persistência da Memória', 'Salvador Dalí', 'Pintura', 9656], ['Nú de Costas', 'Amedeo Modigliani', 'Pintura', 5684], ['Noite de Verão', 'Edward Hopper', 'Pintura', 6151], ['O Filho do Homem', 'René Magritte', 'Pintura', 8843], ['O Quarto de Van Gogh em Arles', 'Vincent van Gogh', 'Pintura', 9343], ['Os Três Músicos', 'Pablo Picasso', 'Pintura', 5863], ['O Nascimento de Cristo', 'Sandro Botticelli', 'Pintura', 8938], ['Abaporu', 'Tarsila do Amaral', 'Pintura', 6997], ['Nu Azul', 'Henri Matisse', 'Pintura', 7190], ["Les Demoiselles d'Avignon", 'Pablo Picasso', 'Pintura', 6087], ['Napoleão Cruzando os Alpes', 'Jacques-Louis David', 'Pintura', 9197], ['Nenúfares', 'Claude Monet', 'Pintura', 7923], ['A Última Ceia', 'Tintoretto', 'Pintura', 8309], ['A Arte da Pintura', 'Johannes Vermeer', 'Pintura', 9118], ['Auto-Retrato com Cachimbo', 'Frida Kahlo', 'Pintura', 6022], ['O Lavrador de Café', 'Candido Portinari', 'Pintura', 6431], ['La Grande Jatte', 'Georges Seurat', 'Pintura', 5929], ['Moisés e os Dez Mandamentos', 'Rembrandt', 'Pintura', 9440], ['Os Amantes', 'René Magritte', 'Pintura', 6542], ['Cabeça de Medusa', 'Caravaggio', 'Escultura', 8301], ['Primavera', 'Sandro Botticelli', 'Pintura', 7865], ['O Guitarrista Cego', 'Pablo Picasso', 'Pintura', 9658], ['Alegoria da Primavera', 'Sandro Botticelli', 'Pintura', 5831], ['A Menina com um Brinco de Pérola', 'Johannes Vermeer', 'Pintura', 7564], ['O Grito', 'Edvard Munch', 'Pintura', 9575], ['Os Girassóis', 'Vincent van Gogh', 'Pintura', 5297], ['O Gato', 'Wassily Kandinsky', 'Escultura', 9375], ['O Banho Turco', 'Jean-Auguste-Dominique Ingres', 'Escultura', 7113], ['Retrato de Adele Bloch-Bauer I', 'Gustav Klimt', 'Pintura', 9101], ['Nenúfares e Ponte Japonesa', 'Claude Monet', 'Pintura', 9689], ['O Beijo', 'Gustav Klimt', 'Pintura', 5002], ['A Dama com Arminho', 'Leonardo da Vinci', 'Pintura', 5577], ['As Meninas', 'Diego Velázquez', 'Escultura', 5183], ['O Leão Moribundo', 'Rosa Bonheur', 'Escultura', 8153], ['Guernica', 'Pablo Picasso', 'Pintura', 5978], ['O Touro', 'Pablo Picasso', 'Escultura', 5381], ['Dama Com Unicórnio', 'Raphael', 'Pintura', 7908], ['Moça Lendo uma Carta à Luz de uma Janela Aberta', 'Johannes Vermeer', 'Pintura', 9578], ['A Última Ceia', 'Salvador Dalí', 'Pintura', 6530]]

indice = len(teste1)

listaObra = []
artista = [0]
for i in range(50):
    obra = str.upper(teste1[i][0])
    artista = str.upper(teste1[i][1])
    tipo = str.upper(teste1[i][2])
    valor = float(teste1[i][3])
    agrupamento = (obra, artista, tipo, valor)
    listaObra.append(agrupamento)

pitura = 0
escultura = 0
for i in range(50):
    if listaObra[i][2] == "PINTURA":
        pitura += 1
    else:
        escultura += 1

if pitura > escultura:
    print("Há mais pinturas que esculturas")
else:
    print("Há mais esculturas que pinturas")