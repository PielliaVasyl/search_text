from django import forms

from .models import Search

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ["searching_text", "email"]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

    def clean_searching_text(self):
        searching_text = self.cleaned_data.get('searching_text')
        return searching_text