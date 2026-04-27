import pandas as pd

df = pd.read_csv("data/students.csv")

print(df)

print("\nAverage Math Score:")
print(df["Math"].mean())

topper = df.loc[df["Math"].idxmax()]

print("\nTopper:")
print(topper)