import urllib.request
import json

def get_weather():
    city = input("Enter city name: ")
    url = f"https://wttr.in/{city}?format=j1"
    try:
        req = urllib.request.urlopen(url)
        data = json.loads(req.read().decode())
        current = data['current_condition'][0]
        temp_c = current['temp_C']
        desc = current['weatherDesc'][0]['value']
        print(f"\n🌤️ Current Weather in {city.capitalize()}: {desc}, {temp_c}°C\n")
    except Exception as e:
        print("\n❌ Could not fetch weather. Check city name or connection.\n")

if __name__ == "__main__":
    get_weather()
