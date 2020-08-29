from django import forms
from .models import Post


class PostForm(forms.ModelForm):

        class Meta:
            model = Post
            #image is new
            fields = ('title', 'text')