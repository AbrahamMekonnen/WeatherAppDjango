import requests
from django.shortcuts import render, redirect
from .models import City#imports module from modely.py
from .forms import CityForm #imports cityform or the data of the name and city form forms.py
# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=ab429c4af4709d1f23a5dcf9f87d9094'#pulls data fromt this url and includes a query that allows a user to search through it when they enter a city name in the search box
    err_msg = ''
    message = ''
    message_class = ''
    
    if request.method == 'POST':
        form = CityForm(request.POST)#instatiates the form 
        
        if form.is_valid():#the form is always gonna be valid
            new_City = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name = new_City).count()#counts the number to check if its's over one
            if existing_city_count == 0: # if the existing data is over one, that meeans the city has already been added to the data base, vice-vesa it would run
                r = requests.get(url.format(new_City)).json()#gets the the name 
                print(r)
                if r['cod']==200: # checks if the entered city name exists in teh resource if it does will add the city name otherwise, it will show a popup error 
                    form.save()
                else: 
                    err_msg = 'City already exists or doesnt exists in the world! '
             
            else: 
                err_msg = 'City already exists in the database doesnt exists in the world!'
        
        if err_msg:# if message exists, it would show a red pop-up with an error message. if the string is empty it will return false and shows a succsful pop-up
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City added successfully! '
            message_class = 'is-success'
        
    form = CityForm()#resets the city form
    
    weather_data = []

    cities = City.objects.all()
    for city in cities:#loops through the city to appeand it into weatehr data
        r = requests.get(url.format(city.name)).json()#gets the data form the source file and converts it into dictionary
        
        city_weather = {'city': city.name, 
                    'temperature': r['main']['temp'],
                    'description': r['weather'][0]['description'], 
                    'icon':  r['weather'][0]['icon']}
       
        weather_data.append(city_weather)# saves the data
    print(weather_data)   
    context = {'weather_data' : weather_data, 'form': form, 'message': message, 'message_class': message_class} # stores the data, the reset value, and and the form data
    return render(request, 'weather\weather.html', context)#renders the template based on the context data 

        
        