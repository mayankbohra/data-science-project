import pandas as pd
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(20,5))
df=pd.read_csv("Growth of MSME.csv")

plt.plot(df["Year"],df["Industry Sector"],color="red", marker="o" ,label="Industry Sector")
plt.plot(df["Year"],df["MSME Sector"],color="blue", marker="o", label="MSME Sector")

labels= ax.get_xticklabels()
plt.xlabel("Year")
plt.ylabel("Growth Percentage")
plt.grid(True)
plt.legend()
plt.show()