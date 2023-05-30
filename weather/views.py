from django.shortcuts import render
from django.views import View
import requests
from django.contrib.gis.geoip2 import GeoIP2
from django.template.defaulttags import register

# Create your views here.

@register.filter(name="get_value")
def get_value(dictionary, key):
    return dictionary.get(key)


class WeatherView(View):
    def get(self, request):
        api_url = "http://api.weatherapi.com/v1/current.json?key=f60f1ce470024b06843193509232305&lang=pl&q="
        wether_res = requests.get(api_url+"Warszawa")

        
        #current_user_ip = request.META.get('HTTP_X_FORWARDED_FOR')


        if wether_res.ok == True:
            data = wether_res.json()

            location = data['location']
            current_w = data['current']
            condition = data['current']['condition']

            


            name = location['name']
            country = location['country']
            tz_id = location['tz_id']
            localtime = location['localtime']

            temp_c = current_w['temp_c']

            text = condition['text']
            icon = condition['icon']
            code = condition['code']

            context = {
                "is_location": True,

                "name" : name,
                "country" : country,
                "tz_id" : tz_id,
                "localtime" : localtime,

                "temp_c" : temp_c,

                "text":text,
                "icon":icon,
                "code":code,
            }
        else:
            
            context = {
                "is_location": False
            }


        return render(request, "weather/index.html", context)

    def post(self, request):

        city = request.POST['city-post']

        api_url = "http://api.weatherapi.com/v1/current.json?key=f60f1ce470024b06843193509232305&lang=pl&q="
        wether_res = requests.get(api_url + city)

        
        #current_user_ip = request.META.get('HTTP_X_FORWARDED_FOR')


        if wether_res.ok == True:
            data = wether_res.json()

            location = data['location']
            current_w = data['current']
            condition = data['current']['condition']

            name = location['name']
            country = location['country']
            tz_id = location['tz_id']
            localtime = location['localtime']

            temp_c = current_w['temp_c']

            text = condition['text']
            icon = condition['icon']
            code = condition['code']


            context = {

                "is_location": True,

                "name" : name,
                "country" : country,
                "tz_id" : tz_id,
                "localtime" : localtime,

                "temp_c" : temp_c,

                "text":text,
                "icon":icon,
                "code":code,
            }
        else:
            context = {
                "is_location": False
            }

        return render(request, "weather/index.html", context)

"""

name - Warszawa region - country - Poland lat - 52.25 lon - 21.0 tz_id - Europe/Warsaw localtime_epoch - 1685112041 localtime - 2023-05-26 16:40

last_updated_epoch - 1685111400
last_updated - 2023-05-26 16:30
temp_c - 21.0
temp_f - 69.8
is_day - 1
condition - {'text': 'Słonecznie', 'icon': '//cdn.weatherapi.com/weather/64x64/day/113.png', 'code': 1000}
wind_mph - 11.9
wind_kph - 19.1
wind_degree - 290
wind_dir - WNW
pressure_mb - 1021.0
pressure_in - 30.15
precip_mm - 0.0
precip_in - 0.0
humidity - 46
cloud - 0
feelslike_c - 21.0
feelslike_f - 69.8
vis_km - 10.0
vis_miles - 6.0
uv - 6.0
gust_mph - 11.6
gust_kph - 18.7


text - Słonecznie
icon - //cdn.weatherapi.com/weather/64x64/day/113.png
code - 1000

"""