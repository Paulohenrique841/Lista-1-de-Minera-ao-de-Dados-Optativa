# exercício 6.4

print( 'Calculdora ')
print ('Digite uma opção :\n1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão')

op= int(input('opção : '))

a=float(input("Qua  o valor de A: "))
b=float(input("Qua  o valor de B: "))

if op == 1:
    print('a + b = ', a+b)
elif op == 2:
    print(" a-b = ",a-b)
elif op == 3:
    print ("a * b = ", a*b)
elif op == 4:
    print(" a / b = ",a/b)
else:
    print("opção invalida")


    