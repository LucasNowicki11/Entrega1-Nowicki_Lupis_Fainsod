from unicodedata import east_asian_width
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class actualizarPerfil(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ingresa tu nombre'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ingresa tu apellido'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Número de telefono'}))
    imagen = forms.ImageField()
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'contanos algo sobre vos'}))
    web = forms.URLField(widget=forms.URLInput(attrs={'placeholder':'Ingresa tu página web'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Ingresa tu email'}))


    class Meta:
        model = User
        fields = ['nombre', 'apellido', 'telefono', 'imagen', 'descripcion', 'web']
        
    def __init__(self, *args, **kwargs):
        super(actualizarPerfil, self).__init__(*args, **kwargs)
        self.fields['telefono'].required = False
        self.fields['imagen'].required = False
        self.fields['descripcion'].required = False
        self.fields['web'].required = False
        
class actualizarUsuario(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Ingresa tu contraseña'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Volve a ingresar tu contraseña'}))
    
    class Meta:
        model = User
        fields = ['password1', 'password2']
        help_texts = {k:'' for k in fields}