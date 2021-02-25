import pandas as pd

cars = {
    'Brand': ['Honda', 'Toyota', 'Ford', 'Audi'],
    'Price': [22000, 25000, 27000, 80000]
}
age = [48, 45, 63, 30]
name = ['asc', 'cdrt', 'pwqs', 'kjaha']
df = pd.DataFrame(cars)

# dictionaries list in pandas
lst = [
    {'name': 'aurjub', 'age': 32, 'sex': 'M'},
    {'name': 'shaha', 'age': 22, 'sex': 'F'},
    {'name': 'shopn', 'age': 35, 'sex': 'M'},
]

df_mult = pd.DataFrame(list(zip(name, age)), columns=['Name', 'Age'])
df_dic = pd.DataFrame(lst, columns=['Name', 'Age', 'SEX'])
print(df_dic)
