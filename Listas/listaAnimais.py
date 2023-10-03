# Importando a biblioteca random para gerar idades aleatórias
import random

# Lista vazia para armazenar as informações dos animais
animais = []

# Espécies de animais
especies = ["Leão", "Tigre", "Elefante", "Girafa", "Cobra", "Macaco", "Urso", "Hipopótamo", "Rinoceronte", "Zebra"]

# Preenchendo a lista com informações fictícias
for _ in range(100):
    especie = random.choice(especies)
    nome = f"{especie}-{_}"
    idade = random.randint(1, 20)
    animais.append({"Espécie": especie, "Nome": nome, "Idade": idade})

# Exibindo os primeiros 5 animais como exemplo
for animal in animais[:5]:
    print(f"Espécie: {animal['Espécie']}, Nome: {animal['Nome']}, Idade: {animal['Idade']}")
