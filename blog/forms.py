from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "category"]

    # Field-level validation for 'title'
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 5:
            raise forms.ValidationError("Minimum 5 characters required")
        return title

    # Forms-level validation
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")

        if title and content:
            if title in content:
                raise forms.ValidationError(
                    "The title should not be part of the content."
                )
        return cleaned_data

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
