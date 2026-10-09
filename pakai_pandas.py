import pandas as pd

df = pd.read_csv("nilai.csv")
print(df.groupby("kelas")["nilai"].mean())
print(df[df["nilai"] >= 75]["nama"].tolist())
print(df.sort_values("nilai").tail(1))