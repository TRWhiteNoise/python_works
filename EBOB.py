def bolen(a,b):
    tam_bolenler_ortak=[]
    for i in range(2,a+1):
        if (a % i == 0 and b % i ==0):
            tam_bolenler_ortak.append(i)
    for j in range(i,b+1):
        if (a % j == 0 and b % j ==0):
            tam_bolenler_ortak.append(j)
    tam_bolenler_ortak.sort()
    tam_bolenler_ortak.reverse()
    if tam_bolenler_ortak==[]:
        print("Ortak Bölen Bulunmamaktadır.")
    
    else:
        print(s1,s2, "Sayılarının Ortak Katları :",tam_bolenler_ortak)
        print(s1,s2,"Sayılarının Ebobu:", tam_bolenler_ortak[0])
    
    return tam_bolenler_ortak



while True:
    s1=int(input("1. Sayıyı Giriniz:"))
    s2=int(input("2. Sayıyı Giriniz:"))
    if (s1>0 and s2>0):
        bolen(s1,s2)
    else:
        print("Hatalı Sayı Girdiniz!")


    