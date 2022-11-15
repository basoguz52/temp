import matplotlib.pyplot as plt
import pandas as pd

veriseti = pd.read_csv('kc_house_data.csv')


y = veriseti.price
x = veriseti.sqft_living


plt.scatter(x, y, color="green")
plt.xlabel("sqtf_living")
plt.ylabel("Ev Fiyatı")
plt.show()


def maaliyetfonksiyonu(x,y,theta):
    print(x[0])
    print(y[0])
