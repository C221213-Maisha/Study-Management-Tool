# users/forms.py
from django import forms
from .models import User

class UserRegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput,
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")

        return cleaned_data
