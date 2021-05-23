def ekok_bulma(sayı1,sayı2):
    ekok = 1
    
    for i in range(1,100):
        a=sayı1*i
        for j in range(1,100):
            b=sayı2*j
            if (a == b):
                ekok=sayı1*i
                return ekok
                
while True:
    sayı1 = int(input("Sayı-1:"))
    sayı2 = int(input("Sayı-2:"))

    print("Ekok:",ekok_bulma(sayı1,sayı2))    