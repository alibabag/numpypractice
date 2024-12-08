import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(-10,9,20)

y = x **3
z = x **2


'''
figure = plt.figure()

axes = figure.add_axes([0.1,0.2,0.7,0.7])
axes.plot(x,y,color="blue")
axes.set_xlabel("X-axis")
axes.set_ylabel("Y-axis")
axes.set_title("Cubed Graph")

axes2 = figure.add_axes([0.2,0.6,0.3,0.3])
axes2.plot(x,z,color="red")
axes2.set_xlabel("X-axis")
axes2.set_ylabel("Y-axis")


plt.tight_layout()
'''
'''
figure = plt.figure()

axes = figure.add_axes([0.2,0.2,0.7,0.7])
axes.plot(x,y,color="blue",label="cubed")
axes.plot(x,z,color="red",label="squared")

axes.legend(loc="upper right")

'''



fig,axes = plt.subplots(nrows=2,ncols=2,figsize=(5,5))
axes[0,0].plot(x,y,color="blue")
axes[0,0].set_title("Cubed Graph")
axes[0,1].plot(x,z,color="red")
axes[0,1].set_title("Squared Graph")

plt.tight_layout()
#fig.savefig("my_first_figure.png")kaydetmek icin


plt.show()