#exercício 7.4

lista1 = []
lista2 = []

produtovetorial = []
produtoescalar = 0

for i in range(3)
    lista1.append(float(input('Digite o {} valor do 1º vetor: '.format(i+1))))
for i in range(3):
    lista2.append(float(input('Digite o {} valor do 2º vetor: '.format(i+1))))
for i in range(3):
    produtoescalar += lista1[i]*lista2[i]



produtovetorial.append(lista1[1]*lista2[2] - lista1[2]*lista2[1])
produtovetorial.append(lista1[0]*lista2[2] - lista1[2]*lista2[0])
produtovetorial.append(lista1[0]*lista2[1] - lista1[1]*lista2[0])



print('Produto escalar:',produtoescalar)
print('Produto vetorial:',produtovetorial)