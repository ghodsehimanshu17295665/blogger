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
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        word_count = len(content.split())
        if word_count > 500:
            raise forms.ValidationError('content should not exceed more than 500 words. It currently have {} words.'.format(word_count))
        return content
