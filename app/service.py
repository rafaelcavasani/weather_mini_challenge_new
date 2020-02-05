import json, requests
from datetime import datetime
from functools import reduce
from itertools import groupby

class Weather:

    def __init__(self):
        self.__api_url = 'http://api.openweathermap.org/data/2.5/forecast?id=6322515&appid=bf9221c4b0dc55fd1a05d6267d37281b'

    def get_weather(self):
        response = requests.get(self.__api_url)
        if response.status_code == 200:
            resp = response.json()
            list_total = resp["list"]
            day_list = list(filter(lambda x: x['main']['humidity'] > 70, list_total))
            days = list(map(lambda x: self.get_week_day(x['dt_txt']), day_list))
            days = list(dict.fromkeys(days))
            ret_str, need_umbrella = self.check_umbrella(days)
            return {"days": ret_str, "need_umbrella": need_umbrella}
        else:
            return {"error": "Erro ao conectar com a API."}
        
    def get_week_day(self, full_date):
        current_date = datetime.strptime(full_date, '%Y-%m-%d %H:%M:%S')
        return current_date.strftime('%A')

    def check_umbrella(self, days):
        if days:
            ret_str = "You need a umbrella this days: "
            ret_str += ", ".join(days)
            arr = ret_str.rsplit(', ', 1)
            ret_str = " and ".join(arr)
            return ret_str, True 
        else:
            return "You don't need a umbrella!!!", False

