import json
import requests as req
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")
gemini_key = os.getenv("GEMINI_API_KEY")

city=input("Enter your city name : ")

# Weather API
url_weather=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metrics"
res_weather=req.get(url_weather)
weather_data=res_weather.json()


## Gemini API 
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent"

headers = {
    "x-goog-api-key": gemini_key,
    "Content-Type": "application/json"
}

data = {
    "contents": [
        {
            "parts": [
                {
                    "text": f"""
                               Act like a weather analyst with 30 years of experience.
                               Tell us what to eat, what to wear as per the weather.
                               weather:{weather_data}  
                            """
                }
            ]
        }
    ]
}

res = req.post(url, headers=headers, json=data)
print(res.json())

# Extract just the text
result = res.json()
suggestion_text = result["candidates"][0]["content"]["parts"][0]["text"]
print(suggestion_text)