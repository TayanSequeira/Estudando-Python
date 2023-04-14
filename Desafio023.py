n1 = int(input('Coloque um número entre 0 e 9999: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('Unidade: ',u)
print('Dezena: ',d)
print('Centena: ',c)
print('milhar: ',m)