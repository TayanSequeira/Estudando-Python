print('Calculador de desconto automático para 5% \n (Colocar o valor do produto separado por ponto)')
n1 = float(input('Qual o preço do produto ?'))
f = n1 * (5/100)
d = n1 - f
print('O valor com o desconto é de: R$', d)