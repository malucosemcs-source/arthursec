import math
angulo=float(input('digite um angulo qualquer'))

seno=math.sin(math.radians(angulo))
coseno=math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))

print('seno: {:.2f}'.format(seno))
print('coseno: {:.2f}'.format(coseno))
print('tangente: {:.2f}'.format(tangente))
