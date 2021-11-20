# exercício 6.5
n = int (input("Digite o numero a qual vai ser fatoriado\n"))

i = 2

while i <= n:
    if n%i == 0:
        print(i, end = ' ')
        n//=i
    else:
        i+=1

