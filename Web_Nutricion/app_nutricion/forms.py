from django import forms
from django.contrib.auth.models import User
from .models import Clientes

class Client_form(forms.Form):
    name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=40)
    birth_date = forms.DateField()
    age = forms.IntegerField()
    sexo = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=100)
    
class Evaluacion_form(forms.Form):
    name_evaluacion = forms.CharField(max_length=50)
    age = forms.IntegerField()
    size = forms.FloatField()
    weight = forms.FloatField()
    bodyfat = forms.FloatField()
    musclemass = forms.FloatField()
    IMC = forms.FloatField()


class Recetas_form(forms.Form):
    recipe_name = forms.CharField(max_length=40)
    ingredients = forms.CharField(max_length=200)
    number_of_grams = forms.FloatField()
    amount_of_cholesterol = forms.FloatField()
    vitamins = forms.CharField(max_length=300)
    
class Avatar_form(forms.ModelForm):
    name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=40)
    imagen = forms.ImageField()
    imagen2 = forms.ImageField()
    imagen3 = forms.ImageField()
    imagen4 = forms.ImageField()
    
    class Meta:
        model = User
        fields = ['name', 'last_name', 'imagen', 'imagen2', 'imagen3', 'imagen4']
        helps_texts = {k:'' for k in fields}
        
    def __init__(self, *args, **kwargs):
        super(Avatar_form, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['last_name'].required = False
        self.fields['imagen'].required = False
        self.fields['imagen2'].required = False
        self.fields['imagen3'].required = False
        self.fields['imagen4'].required = False
