from django import forms
from django.contrib.auth.models import User


class PostForm(forms.Form):
    title = forms.Charfield(max_length=200)
    text = forms.Charfield(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=User.objects.all())