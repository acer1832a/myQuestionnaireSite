from django import forms
from .models import Questionnaire_Results

class Results_form(forms.Form):
    gender = forms.ChoiceField(choices=Questionnaire_Results.GENDER_CHOICES, widget=forms.RadioSelect)
