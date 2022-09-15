# from tkinter import *
from style_NewsAp import *
from tkinter import messagebox, StringVar
from tkinter import ttk
# from PIL import Image, ImageTk
import requests


class WeatherApp:
    # noinspection PyGlobalUndefined
    global apiKey, url
    apiKey = 'fd16fbbb17a8f5ac89f69f53675bded6'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

    def __init__(self, root):
        self.root = root
        self.root.title('CheckWeather')
        self.root.geometry('380x460+350+150')
        self.root['bg'] = red
        # self.txt = Label(text='Check Weather', font=('rockwell bold', 16), bg=red, fg='white')
        # self.txt.pack(pady=20)

        citytext = StringVar()
        cityentry = ttk.Entry(root, text=citytext, font=('arial bold', 30),
                              style='EntryStyle.TEntry', justify=CENTER, width=20)
        cityentry.pack(pady=0)
        cityentry.focus()

        def check_weather(city):
            result = requests.get(url.format(city, apiKey))
            if result:
                json = result.json()
                city = json['name']
                country = json['sys']['country']
                temp_kelvin = json['main']['temp']
                temp_celcius = temp_kelvin - 273.15
                temp_farenheit = temp_celcius*(9/5)+32
                icon = json['weather'][0]['icon']
                weather = json['weather'][0]['main']
                final = (city, country, temp_celcius, temp_farenheit, icon, weather)
                return final
            else:
                return None

        def searched_for(app_2):
            print(app_2)
            city = citytext.get()
            print(city)
            weather_t = check_weather(city)
            if weather_t:
                locationlabel['text'] = f'{weather_t[0]}, {weather_t[1]}'
                # cur_dir =
                img['file'] = f'icon\\{weather_t[4]}.png'
                temperaturelabel['text'] = f'{weather_t[2]:.2f} °C, {weather_t[3]:.2f} °F'
                weatherlabel['text'] = f'{weather_t[5]}'
                introlabel.destroy()
            else:
                messagebox.showerror('ERROR', f'Couldn\'t find the city : {city}')
                print(f"Searched for : {city}")

        def press():
            introlabel.destroy()
            searched_for(root)

        searchbutton = Button(root, text='Press enter \n/\nSearchWeather', font=('rockwell bold', 16),
                              width=20, height=4, bg='blue', fg='white', command=press)
        searchbutton.pack(pady=20)

        cityentry.bind('<Return>', searched_for)

        locationlabel = Label(root, text='', bg=red, fg='White', font=('rockwell bold', 30))
        locationlabel.pack()

        introlabel = Label(root, text='Search (City/State/Country)', bg=red, fg='White',
                           font=('rockwell bold', 16))
        introlabel.pack()

        img = PhotoImage(file='')
        image = Label(root, image=img, bg=red, fg='white')
        image.pack()

        temperaturelabel = Label(root, text='', font=('rockwell bold', 21), bg=red, fg='white')
        temperaturelabel.pack()

        weatherlabel = Label(root, text='', font=('rockwell bold', 21), bg=red, fg='white')
        weatherlabel.pack()

    def start_weather():
        app = Toplevel()
        WeatherApp(app)
        app.mainloop()
