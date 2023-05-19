import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv("Growth of MSME.csv")
x= df["Industry Sector"]
y= df["MSME Sector"]

plt.scatter(x,y)
plt.xlabel("Industry Sector")
plt.ylabel("MSME Sector")

plt.plot(np.unique(x), np.poly1d(np.polyfit(x,y,1))(np.unique(x)),color="r")
plt.show()
