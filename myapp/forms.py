from django import forms


class WordForm(forms.Form):
    word = forms.CharField(label="Enter word or phrase for search")
