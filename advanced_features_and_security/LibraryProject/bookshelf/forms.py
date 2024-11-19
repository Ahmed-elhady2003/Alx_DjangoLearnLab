from django import forms
from .models import Book

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)

    def clean_query(self):
        data = self.cleaned_data['query']
        if not data.isalnum():
            raise forms.ValidationError("Invalid input!")
        return data
    ExampleForm