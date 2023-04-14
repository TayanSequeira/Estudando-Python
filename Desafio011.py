print('Não colocar a unidade somente o número.')
l = float(input('Qual a largura da parede em metros ?'))
a = float(input('Qual a altura da parede em metros ?'))
area = l * a
tinta = (l*a) / 2
print('A área dessa parede é igual a: {}m² \n A quantidade de tinta que você terá que usar é {} L'.format(area, tinta))
