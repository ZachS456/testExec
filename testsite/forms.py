from django import forms

    class NameForm(forms.Form):
    your_name = forms.CharField(label='Button', max_length=100)
