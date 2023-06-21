idades = [45,78,36,12,14,95]
nomes = ['Paulo', 'John', 'João', 'Alexander', 'Claudio']

# for i in range(6):
#     print(lista[i])

for indice, nome in enumerate(nomes):
    print(f'Indice: {indice}, Nome: {nome}, Idade: {idades[indice]}')