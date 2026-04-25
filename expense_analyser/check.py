import pandas as pd
df=pd.read_csv('data_set.csv')
df=df.dropna()

df["price"]=df["price"].fillna(df["price"].mean())
#print(df['price'])
df["shop"]=df["shop"].fillna("aviral")
df['date']=pd.to_datetime(df['date'],format="%m-%d-%y",errors='coerce')
df=df.dropna(subset=['date'])

df=df.dropna(subset=['date'])
df=df.drop_duplicates()
df['shop']=df['shop'].str.lower()
df['shop']=df['shop'].str.strip()
df['price']=pd.to_numeric(df["price"],errors='coerce')

df=df[df['price']<500]

print(df.describe())
# print("-------------------")
# print(df)
# print("*******************")
# print(df.head())
# print("*******************")
# print(df.info())
# print("*******************")
# print(df.isnull().sum())
# print("*******************")