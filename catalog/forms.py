from django import forms
from catalog.models import Book

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'