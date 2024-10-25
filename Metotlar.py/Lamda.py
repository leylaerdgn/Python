#toplama=lambda x,y: x+y
#print(toplama(5,3))


#sayilar=[1,2,3,4,5]
#ikiKati=list(map(lambda x:x*2, sayilar))
#print(ciftler)

sayilar=[1,2,3,4,5,6,7,8,9,10]
ciftler=list(filter(lambda x: x%2==0 ,sayilar))
print(ciftler)