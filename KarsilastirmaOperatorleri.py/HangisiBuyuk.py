a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))

result=(a>b) and (a>c)
print(f'En büyük sayı: {a} {result}')

result=(b>a) and (b>c)
print(f'En büyük sayı: {b} {result}')

result=(c>a) and (c>b)
print(f'En büyük sayı: {c} {result}')