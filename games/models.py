from django.db import models
from datetime import datetime    
from django.forms import TextInput, Textarea
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
   # user = models.OneToOneField(User)
    user = models.ForeignKey(User)
   # user = models.ForeignKey(User, default='DEFAULT lala')

    game_text = models.CharField(max_length=150)
    location_text = models.CharField(max_length=100,default='Location')
    contact_text = models.CharField(max_length=100,default='Contact')
    kickoff_date = models.DateTimeField(blank=False)
    #kickoff_datetime = models.DateTimeField(blank=True)
    #kickoff_date = models.DateTimeField(blank=True)
    #kickoff_time= models.DateTimeField(blank=True)
    players_needed = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return self.game_text



