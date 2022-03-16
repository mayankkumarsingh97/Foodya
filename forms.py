from django import forms
from .models import Contactus
from django.forms.widgets import CheckboxInput, Textarea




class FoodyaContactus(forms.ModelForm):
    class Meta:
         model = Contactus
         fields = ['name', 'email','phone','org']
         widgets ={
             'name':forms.TextInput(attrs={'class':'form-control py-3 myClass','placeholder':'*name','pattern':"([a-zA-Z',.-]+( [a-zA-Z',.-]+)*){3,30}"}),
             'email':forms.EmailInput(attrs={'class':'form-control py-3 myClass','placeholder':'*email',}),
             'phone':forms.TextInput(attrs={'class':'form-control py-3 myClass','placeholder':'*phone','pattern':'[789][0-9]{9}'}),
             'org':forms.TextInput(attrs={'class':'form-control py-3 myClass','placeholder':'organization'}),

             
         }

         error_messages = {
            'phone': {
                'pattern': ("This writer's name is too long."),
            },
        }
