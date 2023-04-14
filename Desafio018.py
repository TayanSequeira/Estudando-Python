import math as mt
ang = float(input('Digite o valor do angulo: '))
rad = mt.radians(ang)
print('Esses são os valores de sen, cos e tg do angulo {}º \n sen = {:.2f} \n cos = {:.2f} \n tg = {:.2f}'.format(ang, mt.sin(rad), mt.cos(rad), mt.tan(rad)))