import pandas as pd 
from visualisation import plot_category_spending,plot_daily_trend


def load_data(file_path):
    df = pd.read_csv(file_path)
    df["date"] = pd.to_datetime(df["date"],format='%m-%d-%y',errors="coerce")
    #df=df.dropna(subset=['date'])
    df['price']=df['price'].fillna(df['price'].mean())
    df['shop']=df['shop'].fillna("others")

    return df
# data={
#   "date":["2024-01-01","2024-01-02","2024-01-03","2024-01- 04",],
#    "amount":[100,200,300,400],
#    "description":["food","clothing","entertainment","transportation"]
#  }


# apply function along any axis of dataframe row or column
           






