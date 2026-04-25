#from google import genai
import requests
from collections import deque
import requests
from pymongo import MongoClient
import ollama
import speech_recognition as sr
import pyttsx3






 
#gemini_api_key="AIzaSyDgIObLB4X72MSJX-U8XkKXn31QXUTIV-M"
mongo_connection_string = "mongodb+srv://aavviirraall:aviral11223344@cluster0.uexv73q.mongodb.net/?appName=Cluster0"
weather_api_key = "7b208aba10193b9f6434d7806dd95112"
db_username="avii"
db_password="avii1234"
#gemini_client = genai.Client(api_key=gemini_api_key)
mongo_client = MongoClient(mongo_connection_string)
db = mongo_client["gemini_llm"]
collection = db["talking with the model"]
print("connected")

# def get_weather(city):
#     weather_api_key="7b208aba10193b9f6434d7806dd95112"
#     calling_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={weather_api_key}"
#     response=requests.get(calling_url).json()
#     if "main" in response:  
#         temp = response ["main"]["temp"]
#         desc = response ["weather"][0]["description"]
#         return f"the current temperature in {city} is {temp} degree celcius and the weather is {desc}"
#     else:
#         return " na mila vaha ka mausam"
    
# def is_weather_query(user_input):
#     weather_keywords = ["weather", "temperature", "climate"]
#     return any(keyword in user_input.lower() for keyword in weather_keywords)






    
engine=pyttsx3.init()
engine.setProperty('rate',150)
engine.setProperty('volume',1)


while(True):

    r=sr.Recognizer()
    with sr.Microphone() as source:
   
        audio=r.listen(source)
    try:
        user_input=r.recognize_google(audio)

    except sr.UnknownValueError:
        print("bhai ya behen samajh nahi aaya")
    except sr.RequestError:
        print("error agyii")

    #user_input = input("enter your query:  ")




    response=ollama.chat(
        model="llama3",
        messages=[{"role":"user","content":user_input}],
        
    )
    print(f"ye lo tumhara jawab : {response['message']['content']}")

    if user_input.lower() == "exit":
        print("....")

        break


    
    chat_data = {
        "question":user_input,
        "answer":response["message"]["content"]
    }


    

    collection.insert_one({
        "prompts":user_input,
        "response":response['message']['content']    })


    
