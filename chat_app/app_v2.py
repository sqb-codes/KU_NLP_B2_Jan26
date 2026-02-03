import speech_recognition as sr
import pyttsx3

from datetime import datetime
import webbrowser
import requests
from ddtrace.bootstrap.sitecustomize import source

# Corpus
greet_messages = ["hi", "hello", "hey", "hi there", "hey there"]
date_msgs = ["what's the date","date","tell me date","today's date"]
time_msgs = ["what's the time","time","tell me time","current time"]
news_intent = ["tell me news", "news", "headlines"]

engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = rec.listen(source)
    try:
        query = rec.recognize_google(audio)
        print("Your Query :",query)
        return query.lower()
    except BaseException as ex:
        print("Can't catch that...")
        # print("Exception :",ex)


def get_location():
    response = requests.get("http://ip-api.com/json/")
    data = response.json()
    city = data.get("city", "Unknown location")
    country = data.get("country", "Unknown country")
    return country, city

def get_news():
    api_key = "695e07af402f4b119f0703e9b19f4683"
    news_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response  = requests.get(news_url)
    data = response.json()
    articles = data['articles']
    total_articles = len(articles)
    for i in range(total_articles):
        print(f"Headline {i+1}: {articles[i]['title']}")


chat = True

while chat:
    # msg = input("Enter your message: ").lower()
    msg = listen()

    if msg in greet_messages:
        print("Hello how are you ?")
    elif msg in date_msgs:
        print(datetime.now().date())
    elif msg in time_msgs:
        current_time = datetime.now().time()
        print(current_time.strftime("%I:%M:%S"))
    elif "open" in msg:
        site = msg.split("open ")[-1]
        url = f"https://www.{site}.com"
        webbrowser.open(url)
        print(f"Opening {site}...")
    elif msg in news_intent:
        get_news()
    elif "location" in msg:
        country, city = get_location()
        print(f"Your location is {city}, {country}")
    elif msg == "bye":
        chat = False
    else:
        print("I can't understand")
