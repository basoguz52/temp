
x =[1, 2, 3, 4] 
y =[1, 2, 3, 4]

m = 3


exit = 0

while(exit == 0):
    t0 = float(input("teta 0 değerini giriniz: "))
    t1 = float(input("teta 1 değerini giriniz: "))
    toplam = 0
    for i in range(m):
        fark = (t0 + t1 * x[i]) - y[i]
        toplam += fark **2
    
    sonuc = toplam / (2*m)
    print(sonuc)
    
    
    girdi = input("Devam etmek için 0 girişini yapınız\n")
    exit = int(girdi)
