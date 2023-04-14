km = float(input('Qual a quantidade de KM rodados ? '))
d = float(input('Qual a quantidade de dias alugado ? '))
vkm = km*0.15
vd = d*60
vt = vkm + vd
print('O valor que você paga por quilometragem é de R${:.2f} \n O valor que você paga por dias utilizado é de R${:.2f} \n e o Valor total é de R${:.2f}'.format(vkm, vd, vt))