from django import forms


class RepostForm(forms.Form):
    url = forms.URLField()
    tags = forms.CharField()
    comment = forms.CharField()
