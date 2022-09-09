def calc(n1,sign,n2):
    signs = {
    '/' : lambda n1, n2: n1 / n2,
    '*' : lambda n1, n2: n1 * n2,
    '-' : lambda n1, n2: n1 - n2,
    '+' : lambda n1, n2: n1 + n2,
    '^' : lambda n1, n2: n1 ** n2,
    }
    result = signs[sign](n1,n2)
    print(f'{result:.2f}')
