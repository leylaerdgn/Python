#def add(*params):
#    return sum((params))
#print(add(10,20))
#print(add(10,20,30))


def displayerUser(**args):
    for key,value in args.items():
     print('{} is{}'.format(key,value))

displayerUser(name="Çınar", age=2, city="İstanbul")
displayerUser(name="Leyla", age=19,city="Batman",phone=123)
