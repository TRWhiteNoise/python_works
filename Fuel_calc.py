#Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
a=float(input("Yakıt Tüketimi(litre/100km):"))
b=float(input("Gidilen Yol(km):"))
c=float(input("Yakıt Birim Fiyatı:"))
d=float(a*b*c/100)
print("Aracınızla {:.1f} km yol yaptığınızda, maliyet: {:.2f} TL dir.".format(b,d))