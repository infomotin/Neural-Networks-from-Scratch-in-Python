import pandas as pd

df = pd.read_csv('./src/pandas/data.csv')
# print(df.shape)
# row, col = df.shape
# print(row, ' ', col)
# print(df[5:80])

# print(df.columns)
# print(df["EMP_NAME"])
# print(df.EMP_NAME)
# print(df.head())
# print(df[['CARD_NO', 'EMP_NAME', 'DESIG_NAME', 'GROSS_SAL', 'BANK_AMT']])
# print((to_int(df['BANK_AMT']).mean()))
# print(df.describe())
# print(int(df[df["GROSS_SAL"]]) > 30000)

# print(df[df["GROSS_SAL"].str.replace(',', '')] > 30000)

print(df.loc[:8])
print(df.iloc[:8])
