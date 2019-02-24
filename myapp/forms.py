from django import forms


class WordForm(forms.Form):
    word = forms.CharField()
