from django import forms

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
    
class Avatar_form(forms.Form):
    name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=40)
    birth_date = forms.DateField()
    age = forms.IntegerField()
    sexo = forms.CharField(max_length=20)
   
   