from django import forms

class TechForm(forms.Form):
    facility = forms.ChoiceField()
    equipment_name = forms.ChoiceField()
    TML = forms.ChoiceField()
    Reading = forms.FloatField(max_value=1)

class CreateEquipmentForm(forms.Form):
    equipment_name = forms.ChoiceField()

class ViewEquipmentData(forms.Form):
    equipment_name = forms.ChoiceField()
