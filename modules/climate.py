import requests, json
import time
import os
import time

def error_log(exception_):
    named = time.localtime()
    time_string = time.strftime("%m-%d-%Y_%H-%M", named)
    path = r'logs'  # to logs folder
    file_name = 'error_log_%s.txt' % time_string
    file = os.path.join(path, file_name)
    file = open(file, "a")  # creates the new file if not exists
    file.write(str(exception_))  # write the exception on the new file
    file.close()

class Weather:
    def __init__(self, place):
        self.place = place
    def get_weather(self):
        try:
            api_key = "083d17f0b6d04f05a4a3f7b7ea39e163"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            city_name = str(self.place)
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name

            response = requests.get(complete_url) 
            x = response.json() 

            if x["cod"] != "404": 
                y = x["main"] 
            
                current_temperature = y["temp"] 
                current_temperature = round(int(current_temperature) - 273.15, 1)
                
                current_pressure = y["pressure"] 
                current_humidiy = y["humidity"] 
                z = x["weather"] 
                
                return "La temperatura en {city}, es de {temp} grados celcius, la presión atmosférica de {pres} hecto pascales, y la humedad de {hum} porcientos".format(city=self.place, 
                    temp=str(current_temperature), pres=str(current_pressure), hum=str(current_humidiy))

            else: 
                return "Ciudad no encontrada"
        except Exception as ex:
            error_log(ex)
