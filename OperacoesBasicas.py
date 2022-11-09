def operations(a, b):
    adi = a + b
    print('O valor da soma de {} e {} é {},'.format(a, b, adi))

    sub = a - b
    print('O valor da subtração de {} e {} é {},'.format(a, b, sub))

    mult = a * b
    print('O valor da multiplicação de {} e {} é {},'.format(a, b, mult))

    div = a / b
    print('E o valor da divisão de {} e {} é {:.2f}.'.format(a, b, div))


a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número: '))
operations(a, b)