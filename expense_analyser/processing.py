from main import load_data
from visualisation import plot_category_spending,plot_daily_trend
from intelligence import intelligence,budget_fix
from patterns import day_wise
from machine_learning import vectorizer,model
import joblib

model=joblib.load("model.pkl")
vectorizer=joblib.load("vectorizer.pkl")
df=load_data("data_set.csv")

def processing():
    print("-------hello to our expense analyser app using machine learning-------")
    print("//////////////////////////////////////////////////////////////")
    
    print("***********************************************************")
    df=load_data("data_set.csv")
    def predict_category(shop):
        vector=vectorizer.transform([shop])
        prediction=model.predict(vector)
    
        
        return prediction[0]

    df["predicted_csv"] = df["shop"].apply(predict_category)
     
    
    intelligence()
    budget_fix()
    day_wise(load_data("data_set.csv"))
    
    #df=process_data(df)

    total_spent=df["price"].sum()
    average_spent=df["price"].mean()
    top_spend=df.groupby("predicted_csv")["price"].sum().idxmax()
    print(f"total spent: {total_spent}")
    print(f"average spent: {average_spent}")
    print(f"top spend category: {top_spend}")

    

    
    print(df)
  

    plot_category_spending(df)
    plot_daily_trend(df)
    print("---------------------------------------------------------------------")
  




processing()

