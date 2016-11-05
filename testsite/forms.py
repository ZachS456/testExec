from django import forms
from django.core.validators import MaxValueValidator

class AlgorithmForm(forms.Form):
    name = forms.CharField(label='filename',max_length=100)
    length = forms.IntegerField(label='length',validators=[MaxValueValidator(20)], required=False)
    start = forms.CharField(label='start',max_length=100, required=False)