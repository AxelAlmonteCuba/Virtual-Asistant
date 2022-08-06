import requests



def run_mike(city):
        rec = ""
        if "" in rec:
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=b8f7a5c265ef30de9dbb58449dff901d&units=metric".format(city) #.format importante
            
            
            res = requests.get(url)

            data = res.json()


            temp = data["main"]["temp"]
            wind_speed = data["wind"]["speed"]

            latitude = data["coord"]["lat"]
            longitude = data["coord"]["lon"]

            description = data["weather"][0]["description"]

            response = "La temperatura es: " + str((temp)) +" La velocidad del viento es:" + str(wind_speed) + " La latitud es: " + str(latitude) + " La longitud es: " + str(longitude)
            return response

