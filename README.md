🌦️ LLM Weather Suggestion App

A simple Python app that fetches real-time weather data for a city and uses a Large Language Model (Google Gemini) to generate personalized suggestions on what to wear and eat based on current conditions.

How It Works
User enters a city name.
The app calls the OpenWeather API to fetch current weather data (temperature, humidity, wind, conditions).
That weather data is passed into a prompt sent to the Gemini API.
Gemini responds as a "30-year veteran weather analyst" with practical clothing and food suggestions tailored to the day's weather.
Tech Stack
Python
OpenWeather API — real-time weather data
Google Gemini API — LLM-generated suggestions
requests — API calls
python-dotenv — secure API key management
Setup
1. Clone the repo
bash
git clone https://github.com/Madhanmohan0108/Weather-Suggestion-.git
cd Weather-Suggestion-
2. Install dependencies
bash
pip install requests python-dotenv
3. Add your API keys

Copy the example file and fill in your real keys:

bash
cp .env.example .env

Then edit .env with your actual keys (this file is gitignored and never pushed):

OPENWEATHER_API_KEY=your_openweather_key_here
GEMINI_API_KEY=your_gemini_key_here

You can get keys from:

OpenWeather: https://openweathermap.org/api
Gemini: https://ai.google.dev/
4. Run the app
bash
python index.py

You'll be prompted to enter a city name, and the app will print a weather-based suggestion.

Example Output
Enter your city name : Hyderabad

Looking at the current conditions in Hyderabad — 30°C with 62% humidity —
here's what I'd recommend: light cotton clothing, stay hydrated with
coconut water or buttermilk, and keep meals light...
Security Note

API keys are loaded from a local .env file (excluded via .gitignore) and are never hardcoded or committed to this repository.

Future Improvements
 Add a Streamlit UI for a visual interface
 Support multi-day forecasts instead of just current weather
 Add error handling for invalid city names
 Deploy as a web app
Author

Built by Madhanmohan as a portfolio project exploring LLM + API integration.
