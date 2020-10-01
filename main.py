import requests

HEADERS = {
    'X-Yandex-API-Key': '20d3cd36-6f8e-4486-b0cd-934db7a82722',
    'User-Agent': 'Mozilla/5.0'
}

# city = str(input())
city = 'orenburg'
URL = f'https://api.weather.yandex.ru/v2/forecast?url=https://yandex.ru/pogoda/{city}'


r = requests.get(url=URL, headers=HEADERS).json()
# ==> GET FACT WEATHER DATA-Dictionary
fact = r.get('fact')


# ==> City, temp, humidity, pressure_mm, wind_speed
print(city)
print(f"Температура сейчас: {fact.get('temp')}°C")
print(f"Ощущается как {fact.get('feels_like')}°C")
print(f"Влажность {fact.get('humidity')}%")
print(f"Давление {fact.get('pressure_mm')} мм")
print(f"Скорость ветра {fact.get('wind_speed')} м/c")
