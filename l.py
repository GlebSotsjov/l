From myModul import * #Summa
 
#2
while True:
    try:
        aasta=int(input("Sisesta aasta numer: "))
        break
    except:
        print("viga")
a=is_year_leap(aasta)
print(a)


