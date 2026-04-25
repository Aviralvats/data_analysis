from main import load_data
from machine_learning import predict_category
df=load_data("data_set.csv")
def intelligence():
    print("---------------------------------------------------------------------")
    daily_spend=df.groupby(df["date"])["price"].sum()
    average_daily=daily_spend.mean()
    for day,price in daily_spend.items():
        if price>average_daily*1.5:
            print(f"high spend alert  on {day.date()}: spend ₹{price}")
            print("------------------------------------------------")
        else :
            print(f"spend on {day.date()} is normal: spend ₹{price}")   
            print("------------------------------------------------")
                                                  
def budget_fix():
    df["category"]=df["shop"].apply(predict_category)
    grouped_df=df.groupby("category")["price"].sum()
    while True:
    
            
        try: 
            budget=float(input("enter your monthly budget : ₹ ").replace("₹","").strip())
            if budget<0:
                print("invalid budget")
                continue

            break

        except ValueError:
            print("enter a valid budget",ValueError)
 
      
    yes_no=input("do you want to set budget for each category? (Y/N) : ")
    sum=0
    check_budget_catgory=df.groupby("category")["price"].sum()
    if yes_no.lower()=="y":
        for category in grouped_df.index:
            while True:
                try:
                    input_category=float(input(f"enter budget for {category} : ₹ "))
                    if input_category<0:
                        print("invalid budget")
                        continue
                    break
                
                except ValueError:
                    print("enter a valid budget",ValueError)
                
            print(f"budget for {category} is  ₹ {input_category}")
            sum+=input_category
            
            if input_category>grouped_df[category]:
                print(f"you have exceeded your budget for {category} by ₹{input_category-grouped_df[category]}")
        
        print(f"total budget is $ {sum}")

            

        
        

    monthly_budget=print(f"your monthly budget is : ₹{budget}")
    spent=df["price"].sum()
    if spent==budget :
        print("you have spend yout budget")
    elif(spent>budget):
        print("you have exceeded your budget")
    elif(spent<budget):
        print("you are within your budget")
        print(f"you have ₹{budget-spent}")


