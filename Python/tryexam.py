import matplotlib.pyplot as plt
import pandas as pd

def j(toplam,m):

    
    print(toplam)
    toplam = toplam / (2*m)
    return toplam

def karehata(x, y, teta):

    toplam = 0
    for i in range(x.size):
        fark = (teta[0] + teta[1] * x[i]) - y[i]
        toplam += fark ** 2
        
    return toplam
    ## TOPLAM KARE HATA FONKSİYONU ##

def hesapla(toplam,teta,m,x):
    alpha = 0.00001
    temp1 = teta[0] - alpha * (1/m) * toplam * x
    return temp1

def main():
    
    veriseti = pd.read_csv('kc_house_data.csv')


    y = veriseti.price
    x = veriseti.sqft_living

    m = 21000
    
    teta0 = float(input("teta 0 değerini giriniz: "))
    teta1 = float(input("teta 1 değerini giriniz: "))
    teta = [teta0, teta1]
    
    newteta =[0]

    i = 2
    for i in range (10000):
        print(j(karehata(x,y,teta),m))
        temp1 = hesapla(karehata(x,y,teta),teta,m,x[i])
        teta[1] = temp1
        ##print(i,".Teta[0]: ", teta[0])
        ##newteta.append(temp0)




    plt.scatter(x, y, color="green")
    plt.xlabel("sqtf_living")
    plt.ylabel("Ev Fiyatı")
    plt.show()



    ##plt.plot([x[1], max(x)], [y[0], max(y)], color='blue',markerfacecolor='red',markersize=10,linestyle='dashed')

main()