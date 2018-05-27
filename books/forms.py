from django import forms


class ReviewForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='')


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='')
