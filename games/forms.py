from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime    
from django.forms import ModelForm
from games.models import Game
from django.contrib.admin import widgets
from bootstrap3_datetime.widgets import DateTimePicker

from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from django.forms.widgets import TextInput
from suit.widgets import NumberInput
from suit.widgets import EnclosedInput
from suit.widgets import SuitDateWidget, SuitTimeWidget, SuitSplitDateTimeWidget


class MyRegistrationForm(UserCreationForm):
    #email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', )
        
    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        #user.email = self.cleaned_data['email']
        # user.set_password(self.cleaned_data['password1'])
        #user.set_password('g')
        
        if commit:
            user.save()
            
        return user


class MyLoginForm(UserCreationForm):
    #email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', )
        
    username = forms.CharField(required=True)

    
class JQueryUIDatepickerWidget(forms.DateInput):
    def __init__(self, **kwargs):
        super(forms.DateInput, self).__init__(attrs={"size":10, "class": "dateinput"}, **kwargs)

    class Media:
        css = {"all":("http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.6/themes/redmond/jquery-ui.css",)}
        js = ("http://ajax.googleapis.com/ajax/libs/jquery/1.4.3/jquery.min.js",
              "http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.6/jquery-ui.min.js",)  



class GameForm(forms.ModelForm):
     # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Game
        exclude=('user',)

        #fields = ('title', 'url', 'views')
        fields = ('location_text','players_needed','contact_text','game_text','kickoff_date')

        dateTimeOptions = {
        'format': 'yyyy-mm-dd HH:ii',
        'autoclose': True,
        'showMeridian' : False
        }

        widgets = {
            #Use localization and bootstrap 3
            #'datetime': DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3)
            'kickoff_date': DateTimeWidget(options = dateTimeOptions,   bootstrap_version=3 , attrs={'placeholder': 'Kickoff Date/Time','size':'31'})
          

        }

 
    #game_text = forms.CharField(max_length=4002, help_text="Information",widget=forms.Textarea(attrs={'placeholder': 'Other game information (skill level, price, kit etc.)','rows':2, 'cols':31}))

    #kickoff_date = forms.DateTimeField(help_text="Details")

    game_text = forms.CharField(max_length=4002, help_text="Details",widget=forms.TextInput(attrs={'placeholder': 'Other game info (skill level, price, kit)','size':31}))
    location_text = forms.CharField(required=True,label='location_text',max_length=400, help_text="Location",widget=forms.TextInput(attrs={'placeholder': 'Location of the game','size':'31'}))
    contact_text = forms.CharField(required=True,max_length=100,help_text='Contact',widget=forms.TextInput(attrs={'placeholder': 'Contact details (email or mobile number)','size':'31'}))

    players_needed =forms.IntegerField(required=True, help_text='Spaces',min_value=0,
        max_value=31, widget=forms.TextInput(attrs={'placeholder': 'Number of players you are looking for','size':'31'}))
   

 
class NumberInput(TextInput):
    input_type = 'number'


#Usage
#widgets = (
#    'number_field': NumberInput(attrs={'min': '0', 'max': '10', 'step': '1'}),
#)


#class ContactForm2(forms.Form):
#    sender = forms.EmailField()

#class ContactForm3(forms.Form):
#    message = forms.CharField(widget=forms.Textarea)
    
    
