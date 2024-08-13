
import tkinter as tk
import requests

# your own OpenWeatherMap API key
API_KEY ="8775039cb6233eaaf0567d5a1213a87a"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data.get("cod") == 200:
        weather_description = data["weather"][0]["description"]
        temperature_kelvin = data["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15
        return f"{weather_description.capitalize()}, {temperature_celsius:.1f}°C"
    else:
        return "Error fetching weather data."

def show_weather():
    city = entry_city.get()
    weather_info = get_weather(city)
    label_result.config(text=weather_info)

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("200x200")

# UI elements
label_city = tk.Label(root, text="Enter city:")
entry_city = tk.Entry(root)
button_get_weather = tk.Button(root, text="Search", command=show_weather)
label_result = tk.Label(root, text="",font="bold")

# Layout
label_city.pack()
entry_city.pack()
button_get_weather.pack()
label_result.pack()

root.mainloop()
