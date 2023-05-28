from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Приложение Погоды")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    try:
        city = textfield.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M")
        clock.config(text=current_time)
        name.config(text="Текущая погода")

        # Погода
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=09df85397dd16d5beadee37fc212dc75"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"°C"))
        c.config(text=(condition_translation[condition], "|", "ОЩУЩАЕТСЯ", temp,"°C"))

        w.config(text=(wind,"км/ч"))
        h.config(text=(humidity,"%"))
        d.config(text=description_translation[description])
        p.config(text=(pressure,"mbar"))
    except Exception as e:
        messagebox.showerror("Приложение погоды","Ошибка в названии!")

# Словарь с переводами состояний погоды
condition_translation = {
    "Clear": "Ясно",
    "Clouds": "Облачно",
    "Rain": "Дождь",
    "Thunderstorm": "Гроза",
    "Snow": "Снег",
    "Mist": "Туман",
    "Smoke": "Дым",
    "Haze": "Мгла",
    "Dust": "Пыль",
    "Fog": "Туман",
    "Sand": "Песчаная буря",
    "Ash": "Пепел",
    "Squall": "Шквал",
    "Tornado": "Торнадо"
}

# Словарь с переводами описаний погоды
description_translation = {
    "clear sky": "ясное небо",
    "few clouds": "небольшая облачность",
    "scattered clouds": "рассеянные облака",
    "broken clouds": "облачно с прояснениями",
    "overcast clouds": "пасмурно",
    "light rain": "небольшой дождь",
    "moderate rain": "умеренный дождь",
    "heavy intensity rain": "сильный дождь",
    "very heavy rain": "очень сильный дождь",
    "extreme rain": "экстремальный дождь",
    "freezing rain": "ледяной дождь",
    "light snow": "небольшой снег",
    "moderate snow": "умеренный снег",
    "heavy snow": "сильный снег",
    "sleet": "мокрый снег",
    "shower rain": "ливень",
    "light intensity shower rain": "небольшой ливень",
    "heavy intensity shower rain": "сильный ливень",
    "ragged shower rain": "порывистый ливень",
    "thunderstorm": "гроза",
    "thunderstorm with light rain": "гроза с небольшим дождем",
    "thunderstorm with rain": "гроза с дождем",
    "thunderstorm with heavy rain": "гроза с сильным дождем",
    "thunderstorm with light drizzle": "гроза с моросящим дождем",
    "thunderstorm with drizzle": "гроза с моросящим дождем",
    "thunderstorm with heavy drizzle": "гроза с сильным моросящим дождем"
}

Search_image = PhotoImage(file="search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

Logo_image = PhotoImage(file="logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

Frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)
# Время
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

label1 = Label(root, text="Ветер", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=90, y=400)

label2 = Label(root, text="Влажность", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=230, y=400)

label3 = Label(root, text="Описание", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=550, y=400)

label4 = Label(root, text="Давление", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=390, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, 'bold'))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=90, y=430)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=250, y=430)
d = Label(text="...", font=("arial", 18, "bold"), bg="#1ab5ef")
d.place(x=548, y=430)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=390, y=430)

root.mainloop()
