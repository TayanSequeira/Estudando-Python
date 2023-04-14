n1 = float(input(('Um valor: ')))
n2 = float(input('Outro valor: '))
s = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2 #esse não está encontrando o valor do resto
e = n1 ** n2
print('A soma vale {} \n a subtração vale {} \n a divisão vale {} \n a divisão por número inteiro vale {} \n o resto vale {} \n a potência vale {}'.format(s, sb, m, d, di, r, e))