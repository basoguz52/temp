import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
# os.chdir('')
# os.listdir()

veriseti = pd.read_csv('Kidem_ve_Maas_VeriSeti.csv')

X = veriseti.iloc[:, -2].values
Y = veriseti.iloc[:, 1].values

plt.scatter(X, Y, color = "cadetblue")
plt.xlabel('Kıdem Bilgisi')
plt.ylabel('Maaş Bilgisi')
plt.show()




