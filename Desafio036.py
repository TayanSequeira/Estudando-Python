vc = float(input('Qual o valor da casa ? R$'))
vs = float(input('Qual o valor do seu salário ? R$'))
tempo = float(input('Em quantos anos ele pretende pagar ? '))
mes = tempo*12
prestacao = vc/mes
porc = vs*(30/100)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de RS{:.2f}'.format(vc, tempo, prestacao))
if prestacao >= porc:
    print('Empréstimo negado!')
else:
    print('Empréstimo concedido!')
