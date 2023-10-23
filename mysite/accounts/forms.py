from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','username','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('passwords do not match')
        return cd['password2']
