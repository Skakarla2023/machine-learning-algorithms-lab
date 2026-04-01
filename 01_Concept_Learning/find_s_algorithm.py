# Concept learning means a computer learns a general rule (concept) from examples so it can classify new things correctly.

import pandas as pd

df = pd.DataFrame([
    ["sunny", "hot", "high", "weak", "yes"],
    ["sunny", "cold", "mild", "weak", "yes"],
    ["rainy", "hot", "high", "strong", "no"]
], columns = ["Sky", "Temp", "Humidity", "Wind", "play"])

h = [None, None, None, None, None]

for i in range(len(df)):
    if df.iloc[i,-1] == "yes":
        for j in range(len(h)):
            value = df.iloc[i,j]
            if h[j] == None:
                h[j] = value
            elif h[j] != value:
                h[j] = '?'

print(h)


















