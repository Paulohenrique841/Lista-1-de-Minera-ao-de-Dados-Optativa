#exercício 7.3

frase=input('Digite uma frase :\n')

Nfrase=str()

for i in frase:
    if i.isupper():
        nome= True
        Nfrase += '*'
        continue
    if nome:
        if i.isalpha():
            Nfrase+= '*'
            continue
        else:
            Nfrase += i
            nome = False
    else:
        Nfrase += i
print(Nfrase)