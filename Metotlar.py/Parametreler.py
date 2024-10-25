#def changeName(n):
#    n= 'Ada'
#name='Yiğit'
#changeName(name)
#print(name)

#def add(a,b): 
 #   return sum((a,b))
#print(add(10,20))

#def add(*params):
 #   return sum((params))
#print(add(10,20))

def displayUser(**args):
    for key, value in args.items():
        print('{} is {}'.format(key,value))
displayUser(name="Leyla" , age=19, city="Elazığ")