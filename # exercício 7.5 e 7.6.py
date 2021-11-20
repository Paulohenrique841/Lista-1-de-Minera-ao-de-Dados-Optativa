# exercício 7.5 e 7.6

N= int(input('Insira o numero N:\n'))

L= list()

for i in range (N):
    x=float(input('Insira um numero para a lista :\n '))
    L.append(x)

print(L)

soma=0
min = L[0]
max = L[0]

for i in L:
    soma += i
    if min > i :
        min = i
    if max < i :
        max = i

        
print('Soma =',soma)
print('Media =', soma/N)
print('Maior =', max)
print('Menor =', min)