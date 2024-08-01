from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "category"]

# class PostForm(forms.Form):
#     title = forms.CharField(max_length=255)
#     content = forms.CharField(max_length=255, widget=forms.Textarea)
#     category = forms.ModelChoiceField(queryset=Category.objects.all(),
#                                       label="Category")


# creating a form
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'content', 'category']

# widgets = {
#     'title': forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Enter the title here',
#     }),
# }
