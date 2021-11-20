# exercício 6.1

n=int(input('Ate qual numero da sequencia de fibonacci deseja ? \n'))
f=0
p=1
s=0
print('Indice 1 f = 1')

for i in range (2,n+1):
    f= p + s
    s = p
    p = f
    print ('Indice', i , ' f =', f)

