import pandas as pd
from pandas_profiling import ProfileReport

df= pd.read_csv("Growth of MSME.csv")

#Generate a Report
profile = ProfileReport(df)
profile.to_file(output_file="Growth of MSME.html")