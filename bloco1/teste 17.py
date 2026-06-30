import math
n1=float(input('comprimento do cateto aposto:'))
n2=float(input('comprimento do cateto adjacente:'))
r=math.hypot(n1,n2)
print('a hipotenusa e {:.2f}'.format(r))
