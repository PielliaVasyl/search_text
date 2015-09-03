from django import forms

from .models import Search

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ["searching_text", "email", "t_limit"]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

    def clean_searching_text(self):
        searching_text = self.cleaned_data.get('searching_text')
        return searching_text

    def clean_t_limit(self):
        t_limit = self.cleaned_data.get('t_limit')
        if t_limit < 1:
            raise forms.ValidationError('Time limit should be not less 1')
        return t_limit