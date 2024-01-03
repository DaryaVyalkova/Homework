import pandas as pd
import numpy as np

indexes = ["a", "b", "c", "d", "e"]
columns = [pd.Series(np.arange(5), index=indexes),
           pd.Series(np.arange(5, 10), index=indexes),
           pd.Series(np.arange(10, 15), index=indexes),
           pd.Series(np.arange(15, 20), index=indexes)]
df = pd.DataFrame(columns)

print(f"{df}\n")
print(f"{df.head(3)}\n")
print(f"{df.tail(3)}\n")

df.to_csv("./data.csv")
