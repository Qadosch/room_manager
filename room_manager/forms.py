from django import forms

class RoomForm(forms.Form):
    name = forms.CharField(max_length=256)
    description = forms.TextInput()
    person = forms.CharField(max_length=256)

class HandingOverForm(forms.Form):
    date = forms.DateField()
    person = forms.CharField(max_length=256)
    description = forms.TextInput()
