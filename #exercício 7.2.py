#exercício 7.2

dicionario = {}
lista = []
nome = '-'


while nome != '':
    nome = str(input('Digite um nome: '))
    lista.append(nome)

lista.remove('')

for nome in lista:
    if nome in dicionario:
        dicionario[nome] += 1
    else:
        dicionario[nome] = 1
print(dicionario)