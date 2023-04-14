valor = float(input('Preço das compras: R$'))
print('''Formas de pagamento:
[ 1 ] À vista
[ 2 ] À vista no cartão
[ 3 ] Parcelado em até 2x
[ 4 ] Parcelado em mais de 3x
''')
pag = int(input('Qual será a forma de pagamento ? '))
avista = valor*(1 - 1/10)
cartao = valor*(1 - 5/100)
duasx = valor
dv = valor/2
tresx = valor*(1 + 20/100)

if pag == 1:
    print('O valor a ser pago será: R${:.2f}'.format(avista))
elif pag == 2:
    print('O valor a ser pago será: R${:.2f}'.format(cartao))
elif pag ==3:
    print('O valor total a ser pago será: R${:.2f}. Sendo cada parcela igual à: R${:.2f}'.format(duasx, dv))
else:
    a = int(input('O pagamento será feito em quantas vezes ? '))
    parc3 = tresx / a
    print('O valor total a ser pago será: R${:.2f}. Sendo cada parcela igual à: R${:.2f}'.format(tresx, parc3))