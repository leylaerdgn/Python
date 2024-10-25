def faktoriyel(x):
    x=int(x)
    if x<0:
        raise ValueError('Negatif değer')
    result=1
    for i in range(1,x+1):
        result*=i
    return result

for x in [5, 10, 20, -3, '10a']:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)
