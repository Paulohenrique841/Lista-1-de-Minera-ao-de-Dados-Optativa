#exercício 5.1
n= int(input("Digite o valor que deseja receber : \n"))

nota100 = n//100
n=n%100

nota50 = n//50
n=n%50

nota10=n//10
n=n%10

nota1 = n//1
n=n%1

print('Notas de 100 reais :',nota100)
print('Notas de 50 reais :',nota50)
print('Notas de 10 reais :',nota10)
print('Notas de 1 reais :',nota1)
