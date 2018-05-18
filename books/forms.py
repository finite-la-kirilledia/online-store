from django import forms


class ReviewForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea())


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea())
