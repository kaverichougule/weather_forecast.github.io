from django.shortcuts import render
import requests
import datetime

# Create your views here.
def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Amsterdam'


    appid ='16c32a2ae3e2b1ced1b6673a2d7f55db'
    URL='https://api.openweathermap.org/data/2.5/weather'
    PARAMS={'q': 'amsterdam','appid':appid,'units':'metric'}
    r = requests.get(URL,PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    day = datetime.date.today()

    return render(request,'index.html', {'city':city,'description':description, 'icon':icon, 'temp': temp, 'day':day})

    