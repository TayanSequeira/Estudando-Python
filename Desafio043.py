peso = float(input('Qual a sua massa corporal ? (Kg) '))
altura = float(input('Qual a sua altura ? (m) '))
imc = peso / (altura*altura)
if imc < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')