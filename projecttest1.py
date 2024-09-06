import tkinter as tk
import requests

def get_weather():
    api_key = "fd569fed37aa602ae9c8ee7406610898"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = entry.get()
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main_info = data["main"]
        weather_info = data["weather"][0]

        temperature = main_info["temp"]
        humidity = main_info["humidity"]
        weather_desc = weather_info["description"]

        output_label.config(text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWeather: {weather_desc}")
    else:
        output_label.config(text="City not found")

app = tk.Tk()
app.title("Weather App")

entry = tk.Entry(app, font=("Helvetica", 20))
entry.pack(pady=10)

get_weather_button = tk.Button(app, text="Get Weather", font=("Helvetica", 15), command=get_weather)
get_weather_button.pack()

output_label = tk.Label(app, font=("Helvetica", 15))
output_label.pack(pady=20)

app.mainloop()
