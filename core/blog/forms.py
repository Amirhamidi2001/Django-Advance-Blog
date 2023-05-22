from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "subject", "message"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["author", "title", "content", "tags", "category", "status"]
