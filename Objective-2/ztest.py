import pandas as pd
from statsmodels.stats.weightstats import ztest

pd.read_csv("Growth of MSME.csv")

x= df["Industry Sector"]
y= df["MSME Sector"]

a,b = ztest(x,y,value=0)
print(a,b)
