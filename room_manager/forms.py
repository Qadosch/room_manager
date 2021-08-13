from django import forms

class RoomForm(forms.Form):
    name = forms.CharField(max_length=256, required=False)
    description = forms.CharField(required=False)
    img = forms.FileField(required=False)
    person = forms.CharField(max_length=256, required=False)

class HandingOverForm(forms.Form):
    HandingOverForm = forms.CharField()
    date = forms.DateField(required=False)
    person = forms.CharField(max_length=256, required=False)
    description = forms.CharField(required=False)

class ImageForm(forms.Form):
    ImageForm = forms.CharField()
    immage_id = forms.IntegerField(required=False)
    immage_img = forms.FileField(required=False)
    immage_description = forms.CharField(required=False)
