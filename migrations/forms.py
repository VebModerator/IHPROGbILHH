from django import forms
from django.contrib.auth.models import User


#1 способ
class PostForm(forms.Form):
    title = forms.Charfield(max_length=200, label="Заголовок")
    text = forms.Charfield(widget=forms.Textarea, label="Текст поста")
    author = forms.ModelChoiceField(queryset=User.objects.all(), label="Автор")

#2 способ
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

labels = {
    "title": "Заголовок",
    "text": "Текст поста"
}
    
