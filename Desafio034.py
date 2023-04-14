s = float(input('Qual o valor do seu salário: R$ '))
a1 = s + (s*1/10)
a2 = s + (s*15/100)
if s > 1250.00:
    print('O valor do seu salário com aumento é de R${:.2f}'.format(a1))
else:
    print('O valor do seu salário com aumento é de R${:.2f}'.format(a2))