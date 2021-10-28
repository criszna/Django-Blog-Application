from django import forms
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','body','thumb']

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['body']
