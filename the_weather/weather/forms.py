from django.forms import ModelForm, TextInput#creates a form based on the model and takes the text input as well
from .models import City #imports the city names

class CityForm(ModelForm):
    class Meta: #deifnes a meta class
        model = City 
        fields = ['name']#text input
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Space'})}#access teh widget though the name of the city, and the place holder is the the word that shouws up in the innput box