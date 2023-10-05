# forms.py
from django import forms

class SparqlQueryForm(forms.Form):
    sparql_query = forms.CharField(widget=forms.Textarea)
    endpoint = forms.URLField()
