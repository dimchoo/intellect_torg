from django import forms
from main_app.models import UserEmail


class EmailForm(forms.Form):
    email = forms.EmailField(max_length=180)

    def clean_email(self):
        return self.cleaned_data['email'].lower()

    def save(self):
        new_user_email = UserEmail.objects.create(email=self.cleaned_data['email'])
        return new_user_email




