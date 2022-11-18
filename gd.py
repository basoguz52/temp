import numpy as np

def ort_kare_hata(x,y,teta):
    
    toplam = 0
    
    for i in range(len(x)):
        toplam += ((teta[0] + teta[1] * x[i]) - y[i]) ** 2
        
    print("Ortalama Kare Hatası:", toplam)

def gd(x, y, teta, alpha, epoch):

    m = float(len(x))

    deneme = sum(((teta[0] + teta[1] * x) - y) ** 2)
    print("Deneme with sum: ", deneme)
    
    
    #den = ((teta[0] + teta[1] * x) - y) ** 2
    #print("Deneme : ", den)
    print("Gerçek Toplam Hata: ", sum(teta[0] + teta[1] * x - y))
    
    
    for i in range(epoch):
        
        y_tahmin = (teta[1] * x) + teta[0]
        #print("i.", i, "Toplam Hata:", sum(y_tahmin))
        # Calculating the gradients
        
		#t1_turev = -(2/n) * sum(x * (y-y_tahmin))
		#t0_turev = -(2/n) * sum(y-y_tahmin)
        
        # Updating weights and bias
		#teta0 = teta0 - (learning_rate * t0_turev)
        #teta1 = teta1 - (learning_rate * t1_turev)
        
        t0_turev = - (2/m) * sum(y - y_tahmin) 
        t1_turev = - (2/m) * sum(x * (y - y_tahmin) )
        
        ##############################
        temp0 = teta[0] - alpha * t0_turev
        temp1 = teta[1] - alpha * t1_turev
        
        teta[0] = temp0
        teta[1] = temp1
        
        if(i <= 17):
            print(i+1, "İTERASYON WEİGHT = ", teta[1], ". BİAS = ", teta[0] )
            #print("teta 0 : ", teta[0])
            #print("teta 1 : ", teta[1])
        
    print("Gerçek Toplam Hata: ", sum((teta[0] + teta[1] * x) - y))
    print(i+1, "İTERASYON WEİGHT = ", teta[1], ". BİAS = ", teta[0] )

def main():
    
    x = np.array([1, 2, 3,4])
    y = np.array([2, 4, 10,17])
    
    epoch = 1000000
    alpha = 0.0001
    
    X = np.array([32.50234527, 53.42680403, 61.53035803, 47.47563963, 59.81320787,55.14218841, 52.21179669, 39.29956669, 48.10504169, 52.55001444,45.41973014, 54.35163488, 44.1640495 , 58.16847072, 56.72720806,	48.95588857, 44.68719623, 60.29732685, 45.61864377, 38.81681754])
    Y = np.array([31.70700585, 68.77759598, 62.5623823 , 71.54663223, 87.23092513,78.21151827, 79.64197305, 59.17148932, 75.3312423 , 71.30087989,55.16567715, 82.47884676, 62.00892325, 75.39287043, 81.43619216,60.72360244, 82.89250373, 97.37989686, 48.84715332, 56.87721319])
    
    
    
    teta = []
    
    teta0 = float(input("teta0: "))
    teta1 = float(input("teta1: "))
    teta.append(teta0)
    teta.append(teta1)
    
    gd(X,Y,teta,alpha,epoch)

main()
