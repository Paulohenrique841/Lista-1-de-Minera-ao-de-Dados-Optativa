#exercício 5.2

t= int (input('Qual o tempo total em segundos ? \n'))

segundos = t%60
t//=60
minutos= t%60
t//=60
horas = t

print('O valor equivale a {} horas  {} minutos {}  e segundos'.format( horas, minutos,segundos))


