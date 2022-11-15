def j(toplam,m):

    
    toplam = toplam / (2*m)
    print(toplam)
    return toplam

def karehata(x, y, teta):

    toplam = 0
    m = x.size()
    for i in range(m):
        fark = (teta[0] + teta[1] * x[i]) - y[i]
        toplam += fark ** 2
        
    return toplam
    ## TOPLAM KARE HATA FONKSİYONU ##


def main():
    

    x = [1, 2, 3, 4]
    y = [1, 2, 3, 4]

    m = 4
    teta0 = float(input("teta 0 değerini giriniz: "))
    teta1 = float(input("teta 1 değerini giriniz: "))
    teta = [teta0, teta1]
    
    
    print()
    print(j(karehata(x,y,teta),m))

main()