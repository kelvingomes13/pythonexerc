# ........................EXERCICIO 1.............................

'''cont = 1
maior_num = float(input(f'digitar o {cont} numero: '))
while cont < 5:
    cont += 1
    num = float(input(f'digitar o {cont} numeros:'))
    if num > maior_num:
        maior_num = num
        print(f'\nDentre os cinco numeros digitados, {maior_num} foi o maior.')

# .................. teste de conteudo pesquisado em outras fontes....'''

'''from time import sleep
def maior(*núm):
    cont = maior = 0
    print('<='*30)
    print("Analisando os valores passados...")
    for valor in núm:
        print(f'valor', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
                cont += 1
                print(f'foram informados {cont} valores ao todo.')
                print(f'o maior valor informado foi {maior}.')

programa principal
maior(2, 9, 4, 6, 7, 1)
maior(4, 7, 0)
maior(1,2)
maior(6)
maior()
'''
# .............................EXERCICIO 2............................

'''
num1 = int(input("primerio numero:"))
num2 = int(input("segundo numero:"))
if num1 > num2:
    print(num1)
else:
    print(num2)
'''
# ............................. EXERCICIO 3....................


'''from functools import total_ordering
num = int(input('digite um numero:'))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
        print('{}' .format(c), end='')
print('\n\033[mO numero{} foi divisivel {} vezes' .format(num, tot))
if tot == 2:
    print('e por isso ele é primo!')
else:
    print(' por esse fato ele nao e primo !')
'''
# ........................EXERCICO 4...............................

'''n1 = float(input('salario  do joao:'))

n2 = float(input('salario  da maria:'))

n3 = float(input('salario  da pedro:'))

n4 = float(input('salario  da lucas'))

n5 = float(input('salario  da marco:'))
media = n1 + n2 + n3+n4+n5 / 5
print('a media entre {} e {} é igual a {}'.format(n1, n2, media))

'''
# ........................EXERCICO 5...............................

'''
def MDC(x, y):
    if x < y:
        x, y = y, x
        while y > 0:
            r = x % y
            x = y
            y = r


def main():
    print("MDC entre x e y:")
    x = int(input('digite x:'))
    y = int(input('digite y:'))
    print("MDC=", MDC(x, y))


main()
'''
# ...... testantod outras fontes de pesquisas................
'''def MDC(x, y):
    resto = None
    while resto is not 0:
        resto = x % y
        x = y
        y = x
        return=x
        # ........................error.........................
        '''
