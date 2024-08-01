from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']

        widgets = {
            "content": forms.Textarea(attrs={
                'placeholder': 'Enter the Content'
                })
        }