import pandas as pd

df = pd.read_csv("./Customers.csv", delimiter=';').dropna()
grouped = df.groupby('Profession')['Income'].agg('mean')

print(grouped)
