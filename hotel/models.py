import numbers
from unicodedata import category
from django.db import models

# Create your models here.

class Room(models.Model):
    ROOM_CATEGORIES=(
    ("PRE", "premium"), 
    ("DEL", "deluxe"),
    ("BAS","basic"),    
    ("QUE","Queen"),    
    ("QIN","King"),    
    )

    number = models.IntegerField()
    category = models.CharField(max_length=3, choices = ROOM_CATEGORIES)
    beds = models.IntegerField(default=1)
    capacity = models.IntegerField(default=1)

    def __str__(self) :
        return f'{self.number} , {self.category} , with {self.beds} beds for {self.capacity} people'