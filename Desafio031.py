d = float(input('Qual a distância em quilometros da sua viagem? '))
a = d*0.5
b = d*0.45
if d <= 200:
    print('O valor que você pagará nessa passagem será de: R${}'.format(a))
else:
    print('O valor que você pagará nessa passagem será de: R${}'.format(b))