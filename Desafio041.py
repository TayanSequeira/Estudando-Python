data = int(input('Qual o ano do seu nascimento? '))
if data >= 2014:
    print('Atleta MIRIM')
elif 2014 > data >= 2009:
    print('Atleta INFANTIL')
elif 2009 > data >= 2004:
    print('Atleta JUNIOR')
elif 2004 > data >= 2003:
    print('Aleta SÊNIOR')
else:
    print('Atleta MASTER')