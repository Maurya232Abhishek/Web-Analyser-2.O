import pandas as pd

data=pd.read_csv("Book1.csv")
print(data)

#print(data)
n=len(data)

#data.to_csv("Book1.csv", index=False)
query = data[data["Fileno"]<=3]
print(query.index)

