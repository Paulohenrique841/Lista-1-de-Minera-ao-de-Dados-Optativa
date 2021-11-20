# exercício 4.2
import math
import numpy


angulo = float (input("Digite o angulo que voce deseja: "))
seno=math.sin(numpy.deg2rad(angulo))
print('O angulo de {} tem o valor de Seno de {:.2f}'.format(angulo,seno))

cosseno=math.cos(numpy.deg2rad(angulo))
print('O angulo de {} tem o valor de Cosseno de {:.2f}'.format(angulo,cosseno))

tangente=math.tan(numpy.deg2rad(angulo))
print('O angulo de {} tem o valor de Tangente de {:.2f}'.format(angulo,tangente))


