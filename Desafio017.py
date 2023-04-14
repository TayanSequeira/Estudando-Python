import math as mt
#ca = float(input('Digite o valor do cateto adjacente '))
#co = float(input('Digite o valor do cateto oposto '))
#hip = mt.sqrt(mt.pow(ca, 2)+mt.pow(co, 2))
#print('O valor da Hipotenusa desse triangulo retangulo é: {}'.format(hip))
ca = float(input('Digite o valor do cateto adjacente '))
co = float(input('Digite o valor do cateto oposto '))
hip = mt.hypot(co, ca)
print('O valor da Hipotenusa desse triangulo retangulo é: {}'.format(hip))