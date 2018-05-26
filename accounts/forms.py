from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from accounts.models import User


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'required id': 'id_email_login', 'class': 'form-control custom-form-control', 'placeholder': 'Электронная почта', }),
        max_length=225, label='')
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control custom-form-control', 'placeholder': 'Пароль', 'type': 'password', }),
        max_length=225, label='')


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'required id': 'id_email_reg', 'class': 'form-control custom-form-control',
               'placeholder': 'Электронная почта',
               'margin-bottom': '50px'}),
        label='')
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control custom-form-control', 'placeholder': 'Имя', }), label='')
    surname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control custom-form-control', 'placeholder': 'Фамилия', }),
        label='')
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control custom-form-control', 'placeholder': 'Телефон', }),
        label='')
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control custom-form-control', 'placeholder': 'Пароль', }),
        label='')
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control custom-form-control', 'placeholder': 'Подтвердите пароль', }),
        label='')

    class Meta:
        model = User
        fields = ('email', 'name', 'surname', 'phone')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'surname', 'phone', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
