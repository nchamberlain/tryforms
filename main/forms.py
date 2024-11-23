from django import forms

#create your forms here.

class ExampleForm(forms.Form):
    name = forms.CharField(label="Enter Your Name")
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    date = forms.DateField()

class ClientForm(forms.Form):
    fname = forms.CharField(max_length=30)
    lname = forms.CharField(max_length=40)
    street_addr = forms.CharField(max_length=100)
    city_name = forms.CharField(max_length=40)
    state = forms.CharField(max_length=40)
