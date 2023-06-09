from django import forms

class Form(forms.Form):
    name = forms.CharField(label='Ім\'я')
    email = forms.EmailField(label='Електронна пошта')
