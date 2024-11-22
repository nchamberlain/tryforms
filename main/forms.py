from django import forms

#create your forms here.

class ExampleForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
    date = forms.DateField()