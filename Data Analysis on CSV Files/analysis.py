import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

print(df.head())
print(df.groupby("Product")["Sales"].sum())

df.groupby("Product")["Sales"].sum().plot(kind="bar")
plt.show()
