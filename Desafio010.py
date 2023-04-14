n1 = float(input('Quantos reais você tem na carteira ? R$'))
d = n1 / 3.27
print('Com R${:.2f}, com o dolar valendo R$3,27. \n Você poderá comprar US${:.2f} Dolares'.format(n1, d))