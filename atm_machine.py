# Atm Machine

login_try=2
sys_id="white"
sys_pass="3223"

while True:
    print("*********************\n Welcome to Atm Machine\nPlease Login")
    id=input("Id:")
    password=input("Password:")
    
    if (login_try==0):
        print("Login Attempt Over. . ")
        break
    if (id!=sys_id and password==sys_pass):
        print("Wrong id, Try Again")
        login_try-=1
        continue
    elif(id==sys_id and password!=sys_pass):
        print("Wrong Password, Try Again")
        login_try-=1
        continue
    elif (id!=sys_id and password!=sys_pass):
        print("Wrong id and password, Try Again")
        login_try-=1
        continue
    
    else:
        print("Login Successful.")
    while True:
            print("""How can i help you? sir. Turkish selected. 
            İşlemler;
        1- Bakiye Sorgulama
        2- Para Yatırma
        3- Para Çekme

        Programdan çıkmak için '9' a basınız.
        ******************
        """)
            cash=1000
            process=input("İşlemi Seçiniz: ")
            if (process==9):
                print("Good bye my friend")
                break
            elif (process=="1"):   
                print("Bakiyeniz: {} $".format(cash))
                """ print("1- Ana Menü\n2- Kart İade")
                fm=input("Devam Etmek İstediğiniz İşlemi Seçiniz: ")

                if (fm==1): """

            elif (process=="2"): 
                miktar=int(input("Yatırmak istedğiniz miktar:"))
                cash+=miktar
                print("Bakiyeniz:{} $".format(cash))

            elif (process=="3"):  
                miktar=int(input("Çekmek istediğiniz miktarı giriniz:"))
                if (cash-miktar < 0):
                    print("Yetersiz Bakiye") 
                    continue
                cash-=miktar
                print("Bakiyeniz:{} $".format(cash))
            else: 
                print("Geçersiz işlem")                      



   