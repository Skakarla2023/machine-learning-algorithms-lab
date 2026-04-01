# Concept learning means a computer learns a general rule (concept) from examples so it can classify new things correctly.

import pandas as pd

df = pd.DataFrame([
    ["Sunny","Hot","High","Weak","Yes"],
    ["Sunny","Hot","Normal","Strong","Yes"],
    ["Rainy","Cold","High","Weak","No"]
],columns = ["Sky","Temp","Humidity","Wind","Play"])

h = [None,None,None,None,None]

for i in range(len(df)):
  if df.iloc[i,-1] == "Yes":
    for j in range(len(h)):
      value = df.iloc[i,j]
      if h[j] == None:
        h[j] = value
      elif h[j]!=value:
        h[j] = '?'

print(h)
