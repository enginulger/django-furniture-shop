from django import forms

class iletisimForm(forms.Form):
    email = forms.EmailField()


