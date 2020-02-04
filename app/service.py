import json, requests
from datetime import datetime
from functools import reduce
from itertools import groupby 
# from .models import WeatherModel

def as_weather(d):
    w = WatherModel()
    w.__dict__.update(d)
    return w    

def get_weather():
    api_url = 'http://api.openweathermap.org/data/2.5/forecast?id=6322515&appid=bf9221c4b0dc55fd1a05d6267d37281b'
    response = requests.get(api_url)
    if response.status_code == 200:
        resp = response.json()
        list_total = resp["list"]
        day_list = list(filter(lambda x: x['main']['humidity'] > 70, list_total))
        group_day = list(groupby(day_list, key=lambda x: x['main']['humidity']))
        print(group_day)
    else:
        return {"error": "Erro ao conectar com a API."}
        

def check_umbrela(response):
    resp = response.json()
    list_total = resp["list"]

    ret = []
    umbrella = False
    next_date = ""
    for i, l in enumerate(list_total):
        current_date = datetime.strptime(l["dt_txt"], '%Y-%m-%d %H:%M:%S')
        if l["main"]["humidity"] > 70:
            umbrella = True
        if (i != len(list_total) - 1):
            next_date = datetime.strptime(list_total[i + 1]["dt_txt"],
                                        '%Y-%m-%d %H:%M:%S')
        else:
            next_date = current_date

        if next_date.date() != current_date.date() or next_date == current_date and i == len(list_total) - 1:
            if umbrella == True:
                ret.append(current_date.strftime('%A'))
                umbrella = False

    ret_str = "You need a umbrella this days:"
    if (len(ret) > 0):
        need_umbrella = True
        for i, r in enumerate(ret):
            if (ret_str == "You need a umbrella this days:"):
                ret_str += " " + str(r)
            else:
                if (i == len(ret) - 1):
                    ret_str += " and " + str(r)
                else:
                    ret_str += ", " + str(r)
    else:
        ret_str = "You don't need a umbrella!!!"
        need_umbrella = False

    return { "days": ret_str, "need_umbrella": need_umbrella }

# {
#     'dt': 1580850000, 
#     'main': {
#         'temp': 301.88, 
#         'feels_like': 308.74, 
#         'temp_min': 299.32, 
#         'temp_max': 301.88, 
#         'pressure': 1009, 
#         'sea_level': 1009, 
#         'grnd_level': 949, 
#         'humidity': 86, 
#         'temp_kf': 2.56
#     }, 
#     'weather': [
#         {
#             'id': 500, 
#             'main': 'Rain', 
#             'description': 'light rain', 
#             'icon': '10d'
#         }
#     ], 
#     'clouds': {
#         'all': 100
#     }, 
#     'wind': {
#         'speed': 0.42, 
#         'deg': 129
#     }, 
#     'rain': {
#         '3h': 1.56
#     }, 
#     'sys': {
#         'pod': 'd'
#     },
#     'dt_txt': '2020-02-04 21:00:00'
# }