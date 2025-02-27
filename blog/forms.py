from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("id", "blog", "full_name", "email", "message")
        exclude = ["blog"]