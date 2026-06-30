p = float(input('Qual é o preço do produto? R$ '))
d = float(input('Qual é o desconto do produto (%): '))

r = p - (p * d / 100)

print('Se o produto custa R$ {:.2f} e está com {:.0f}% de desconto, no final ele custará R$ {:.2f}.'.format(p, d, r))