import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''

plt.plot(x,y,color="red",linewidth=2.5,linestyle=":",marker="o",markersize=10,markerfacecolor="blue",label="y=x^2")
plt.axis([0, 6, 0, 30])# [xmin, xmax, ymin, ymax]
plt.title('My first plot')
plt.xlabel('x label',fontsize=14)
plt.ylabel('y label',fontsize=14)
'''
'''
x = np.linspace(0, 2, 100)
plt.plot(x, x, label='linear',color="red")
plt.plot(x, x**2, label='quadratic',color="blue")
plt.plot(x, x**3, label='cubic',color="green")
plt.title('My first plot')

plt.xlabel('x label')
plt.ylabel('y label')   
plt.legend().loc = "upper left"
'''
'''
x = np.linspace(0, 2, 100)

fig,axs = plt.subplots(3)# 3 rows

axs[0].plot(x,x,color="red")# row 1
axs[0].set_title("y=x")

axs[1].plot(x,x**2,color="blue")# row 2
axs[1].set_title("quadratic")

axs[2].plot(x,x**3,color="green")#row 3
axs[2].set_title("cubic")
plt.tight_layout()# to avoid overlapping
'''
'''
x = np.linspace(0, 2, 100)
fig,axs = plt.subplots(2,2)# 2 rows and 2 columns
fig.suptitle("My first plot")
axs[0,0].plot(x,x,color="red")
axs[0,0].set_title("y=x")

axs[0,1].plot(x,x**2,color="blue")
axs[0,1].set_title("quadratic")

axs[1,0].plot(x,x**3,color="green")
axs[1,0].set_title("cubic")

plt.tight_layout()
'''
df = pd.read_csv('/Users/aligultekin/Desktop/All thing/SE/PYTHON NOTES/mattplotlib/nba.csv')

df = df.drop(["Number"], axis=1)
numeric_df = df.select_dtypes(include=[np.number]).groupby(df["Team"]).mean()
numeric_df.plot(subplots=True, legend=True)


df.head(5).plot(subplots=True, legend=True)
plt.tight_layout()

plt.show()