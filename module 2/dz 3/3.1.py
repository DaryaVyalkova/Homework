import pandas as pd

df = pd.read_csv("./Customers.csv", delimiter=';')

filtered = df[(df['Income'] < 30000) & (df['Age'] > 30)]
print(filtered)

filtered2 = df[(df['Work Experience'] > 5) & (df['Profession'] == 'Lawyer')]
print(filtered2)
