from datetime import datetime
import webbrowser
import requests

# Corpus
greet_messages = ["hi", "hello", "hey", "hi there", "hey there"]
date_msgs = ["what's the date","date","tell me date","today's date"]
time_msgs = ["what's the time","time","tell me time","current time"]

# if msg == "hi" or msg == "hello" or msg == "hey there" or msg == "hey":
#     print("Hello how are you ?")
# else:
#     print("I can't understand")

def get_location():
    response = requests.get("http://ip-api.com/json/")
    data = response.json()
    city = data.get("city", "Unknown location")
    country = data.get("country", "Unknown country")
    return country, city

# NEWS_API_KEY = "695e07af402f4b119f0703e9b19f4683"

chat = True

while chat:
    msg = input("Enter your message: ").lower()

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
    elif "location" in msg:
        country, city = get_location()
        print(f"Your location is {city}, {country}")
    elif msg == "bye":
        chat = False
    else:
        print("I can't understand")
