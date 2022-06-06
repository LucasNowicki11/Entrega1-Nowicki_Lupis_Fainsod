from django import forms

class Client_form(forms.Form):
    name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=40)
    birth_date = forms.DateField()
    age = forms.IntegerField()
    sexo = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=100)
    