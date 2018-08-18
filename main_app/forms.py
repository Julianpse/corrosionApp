from django import forms

class HomeForm(forms.Form):
    facility = forms.CharField()
    equipment_name = forms.CharField()
    TML = forms.CharField()
