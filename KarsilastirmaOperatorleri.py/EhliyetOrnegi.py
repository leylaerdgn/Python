name=input("İsminiz: ")
yas=int(input("Yaşınız: "))
egitim=input("Eğitim Durumunuz: ")

if (yas>=18) and (egitim=='lise' or egitim=='üniversite'):
    print("Ehliyet Alabilirsiniz!")
elif yas<18:
    print(f'{yas} yaşında olduğunuzdan dolayı eğitim alamazsınız')
else:
    print('Eğitim durumunuz yetersizdir')