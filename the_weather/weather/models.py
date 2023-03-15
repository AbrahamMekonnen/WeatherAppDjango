from django.db import models

class City(models.Model):#allows us to store a bunch of city names
    name = models.CharField(max_length=25)#length of letter from each city

    def __str__(self):#returns the name of the city
        return self.name

    class Meta:#plural name with cities that include ies
        verbose_name_plural = 'cities'