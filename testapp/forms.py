from django import forms

class LoadForm(forms.Form):
    first = forms.CharField(max_length=255)
    second = forms.CharField(max_length=255)
    content = forms.ImageField(required=False)
    published = forms.BooleanField(required=False)