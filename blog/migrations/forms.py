from django import forms
from django.contrib.auth.models import User


class PostForm(forms.Form):
    title = forms.Charfield(max_length=200, label="Заголовок")
    text = forms.Charfield(widget=forms.Textarea, label="Текст поста")
    author = forms.ModelChoiceField(queryset=User.objects.all(), label="Автор")
    image = forms.ImageField(required=False, label="Изображение")



class NewPostForm(forms.ModelForm):
    class Meta:
        model = PostForm
        fields = ("title", "text")

        labels = {
            "title": "Заголовок",
            "text": "Текст поста"
        }
