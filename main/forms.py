from django import forms

#create your forms here.

class ExampleForm(forms.Form):
    name = forms.CharField(label="Enter Your Name")
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    date = forms.DateField()

