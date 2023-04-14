nasc = int(input('Que ano você nasceu ? '))
a = 2023 - nasc
b = a - 18
c = 18 - a
if nasc > 2005:
    print('Você ainda terá que se alistar no exército! Você poderá se alistar para o exercíto daqui a {} anos!'.format(c))
elif nasc == 2005:
    print('Está na hora de se alistar para o exército!')
else:
    print('Já passou do tempo de você se alistar! Já passou {} anos para seu alistamento'.format(b))