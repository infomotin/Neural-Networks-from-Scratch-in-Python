import pandas as pd

df = pd.read_csv('./src/pandas/data.csv')
# print(df.shape)
# row, col = df.shape
# print(row, ' ', col)
# print(df[5:80])

# print(df.columns)
# print(df["EMP_NAME"])
# print(df.EMP_NAME)
print(df.head())
