from django import forms


class ReviewForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваш отзыв...', }),
                           label='')


class CommentForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваш комментарий...', }), label='')
