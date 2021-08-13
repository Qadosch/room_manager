from django import forms

class RoomForm(forms.Form):
    name = forms.CharField(max_length=256, required=False)
    description = forms.CharField(required=False)
    img = forms.FileField(required=False)
    person = forms.CharField(max_length=256, required=False)

class HandingOverForm(forms.Form):
    date = forms.DateField(required=False)
    person = forms.CharField(max_length=256, required=False)
    description = forms.CharField(required=False)
