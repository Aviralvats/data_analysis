from main import load_data
df=load_data("data.csv")
def day_wise(df):
    df["day"]=df["date"].dt.day_name()
    day_spend=df.groupby("day")["price"].sum()
    print(day_spend)
