v = float(input('Qual a velocidade do carro: '))
m = ((v-80)*7)
if v > 80:
    print('O valor que você deverá pagar de multa é de: R${}'.format(m))
else:
    print('Você estava abaixo do limite da via, nao irá receber multa!')
