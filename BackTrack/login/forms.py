from django import forms

from .models import currentUser

class login_form(forms.ModelForm):
    class Meta:
        model=currentUser
        fields=[
            "username",
            "password",
            "userType"
        ]
        widgets = {
            "userType": forms.HiddenInput()
        }