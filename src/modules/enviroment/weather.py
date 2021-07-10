import requests
import json
import datetime

def weather():
    api_key = "bd29eef97e25b00079ac1ba6acdb8893"

    url = "https://api.openweathermap.org/data/2.5/weather"
    querystring = {"lat":"41.383745","lon":"2.046644","appid":"bd29eef97e25b00079ac1ba6acdb8893","units":"metric","lang":"38"}
    headers = {
        'Cache-Control': 'no-cache'
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    data = json.loads(response.content)
    hora_UTC = datetime.datetime.fromtimestamp(data['dt'])
    amanecer = datetime.datetime.fromtimestamp(data['sys']["sunrise"])
    atardecer = datetime.datetime.fromtimestamp(data['sys']["sunset"])
    print('')
    print('Condiciones climatologicas')
    print('Latitud:', data['coord']['lat'])
    print('Longitud:', data['coord']['lon'])
    print('Temperatura:', data['main']['temp'])
    print('Sensación termica:', data['main']['feels_like'])
    print('Temperatura minima:', data['main']['temp_min'])
    print('Temperatura máxima:', data['main']['temp_max'])
    print('Presión atmosferica:', data['main']['pressure'])
    print('Humedad:', data['main']['humidity'])
    print('Visibilidad:', data['visibility'])
    print('Velocidad del viento', data['wind']['speed'])
    print('Dirección del viento:', data['wind']['deg'])
    print('Abundancia de nubes:', str(data['clouds']['all']) + ' %')
    print('Hora cálculo datos:', hora_UTC.strftime('%d-%m-%Y %H:%M:%S'))
    print('Código país:', data['sys']['country'])
    print('Hora amanecer:', amanecer.strftime('%H:%M:%S'))
    print('Hora atardecer:', atardecer.strftime('%H:%M:%S'))
    print('Población:', data['name'])
    print('Código población:', data['id'])
