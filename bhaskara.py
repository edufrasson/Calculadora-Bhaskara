
print('='*30)
print('Calculadora de bháskara')
print('='*30)
a = float(input('Digite o coeficiente a: '))
b = float(input('Digite o coeficiente b: '))
c = float(input('Digite o coeficiente c: '))
delta = (b ** 2) - (4 * a) * c
bhaskposi = (- b) + delta ** (1/2)
bhaskneg = (- b) - delta ** (1/2)
bhasksolu1 = bhaskposi / (2 * a)
bhasksolu2 = bhaskneg / (2 * a)
if delta >= 0:
    print('='*30)
    print('A solução será: {} e {}' .format(bhasksolu1, bhasksolu2))
    print('='*30)
else:
    {
        print('Delta negativo, solução inválida.')
    }